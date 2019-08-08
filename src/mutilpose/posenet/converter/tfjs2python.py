import json
import struct
import tensorflow as tf
from tensorflow.python.tools.freeze_graph import freeze_graph
import cv2
import numpy as np
import os
import tempfile

from posenet.converter.config import load_config

BASE_DIR = os.path.join(tempfile.gettempdir(), '_posenet_weights')


def to_output_strided_layers(convolution_def, output_stride):
    current_stride = 1
    rate = 1
    block_id = 0
    buff = []
    for _a in convolution_def:
        conv_type = _a[0]
        stride = _a[1]
        
        if current_stride == output_stride:
            layer_stride = 1
            layer_rate = rate
            rate *= stride
        else:
            layer_stride = stride
            layer_rate = 1
            current_stride *= stride
        
        buff.append({
            'blockId': block_id,
            'convType': conv_type,
            'stride': layer_stride,
            'rate': layer_rate,
            'outputStride': current_stride
        })
        block_id += 1

    return buff


def load_variables(chkpoint, base_dir=BASE_DIR):
    manifest_path = os.path.join(base_dir, chkpoint, "manifest.json")
    if not os.path.exists(manifest_path):
        print('Weights for checkpoint %s are not downloaded. Downloading to %s ...' % (chkpoint, base_dir))
        from posenet.converter.wget import download
        download(chkpoint, base_dir)
        assert os.path.exists(manifest_path)

    f = open(manifest_path)
    variables = json.load(f)
    f.close()

    # with tf.variable_scope(None, 'MobilenetV1'):
    for x in variables:
        filename = variables[x]["filename"]
        byte = open(os.path.join(base_dir, chkpoint, filename), 'rb').read()
        fmt = str(int(len(byte) / struct.calcsize('f'))) + 'f'
        d = struct.unpack(fmt, byte)
        d = tf.cast(d, tf.float32)
        d = tf.reshape(d, variables[x]["shape"])
        variables[x]["x"] = tf.Variable(d, name=x)

    return variables


def _read_imgfile(path, width, height):
    img = cv2.imread(path)
    img = cv2.resize(img, (width, height))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(float)
    img = img * (2.0 / 255.0) - 1.0
    return img


def build_network(image, layers, variables):

    def _weights(layer_name):
        return variables["MobilenetV1/" + layer_name + "/weights"]['x']

    def _biases(layer_name):
        return variables["MobilenetV1/" + layer_name + "/biases"]['x']

    def _depthwise_weights(layer_name):
        return variables["MobilenetV1/" + layer_name + "/depthwise_weights"]['x']

    def _conv_to_output(mobile_net_output, output_layer_name):
        w = tf.nn.conv2d(mobile_net_output, _weights(output_layer_name), [1, 1, 1, 1], padding='SAME')
        w = tf.nn.bias_add(w, _biases(output_layer_name), name=output_layer_name)
        return w

    def _conv(inputs, stride, block_id):
        return tf.nn.relu6(
            tf.nn.conv2d(inputs, _weights("Conv2d_" + str(block_id)), stride, padding='SAME')
            + _biases("Conv2d_" + str(block_id)))

    def _separable_conv(inputs, stride, block_id, dilations):
        if dilations is None:
            dilations = [1, 1]

        dw_layer = "Conv2d_" + str(block_id) + "_depthwise"
        pw_layer = "Conv2d_" + str(block_id) + "_pointwise"

        w = tf.nn.depthwise_conv2d(
            inputs, _depthwise_weights(dw_layer), stride, 'SAME', rate=dilations, data_format='NHWC')
        w = tf.nn.bias_add(w, _biases(dw_layer))
        w = tf.nn.relu6(w)

        w = tf.nn.conv2d(w, _weights(pw_layer), [1, 1, 1, 1], padding='SAME')
        w = tf.nn.bias_add(w, _biases(pw_layer))
        w = tf.nn.relu6(w)

        return w

    x = image
    buff = []
    with tf.variable_scope(None, 'MobilenetV1'):

        for m in layers:
            stride = [1, m['stride'], m['stride'], 1]
            rate = [m['rate'], m['rate']]
            if m['convType'] == "conv2d":
                x = _conv(x, stride, m['blockId'])
                buff.append(x)
            elif m['convType'] == "separableConv":
                x = _separable_conv(x, stride, m['blockId'], rate)
                buff.append(x)

    heatmaps = _conv_to_output(x, 'heatmap_2')
    offsets = _conv_to_output(x, 'offset_2')
    displacement_fwd = _conv_to_output(x, 'displacement_fwd_2')
    displacement_bwd = _conv_to_output(x, 'displacement_bwd_2')
    heatmaps = tf.sigmoid(heatmaps, 'heatmap')

    return heatmaps, offsets, displacement_fwd, displacement_bwd


def convert(model_id, model_dir, check=False):
    cfg = load_config()
    checkpoints = cfg['checkpoints']
    image_size = cfg['imageSize']
    output_stride = cfg['outputStride']
    chkpoint = checkpoints[model_id]

    if chkpoint == 'mobilenet_v1_050':
        mobile_net_arch = cfg['mobileNet50Architecture']
    elif chkpoint == 'mobilenet_v1_075':
        mobile_net_arch = cfg['mobileNet75Architecture']
    else:
        mobile_net_arch = cfg['mobileNet100Architecture']

    width = image_size
    height = image_size

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    cg = tf.Graph()
    with cg.as_default():
        layers = to_output_strided_layers(mobile_net_arch, output_stride)
        variables = load_variables(chkpoint)

        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            sess.run(init)
            saver = tf.train.Saver()

            image_ph = tf.placeholder(tf.float32, shape=[1, None, None, 3], name='image')
            outputs = build_network(image_ph, layers, variables)

            sess.run(
                [outputs],
                feed_dict={
                    image_ph: [np.ndarray(shape=(height, width, 3), dtype=np.float32)]
                }
            )

            save_path = os.path.join(model_dir, 'checkpoints', 'model-%s.ckpt' % chkpoint)
            if not os.path.exists(os.path.dirname(save_path)):
                os.makedirs(os.path.dirname(save_path))
            checkpoint_path = saver.save(sess, save_path, write_state=False)

            tf.train.write_graph(cg, model_dir, "model-%s.pbtxt" % chkpoint)

            # Freeze graph and write our final model file
            freeze_graph(
                input_graph=os.path.join(model_dir, "model-%s.pbtxt" % chkpoint),
                input_saver="",
                input_binary=False,
                input_checkpoint=checkpoint_path,
                output_node_names='heatmap,offset_2,displacement_fwd_2,displacement_bwd_2',
                restore_op_name="save/restore_all",
                filename_tensor_name="save/Const:0",
                output_graph=os.path.join(model_dir, "model-%s.pb" % chkpoint),
                clear_devices=True,
                initializer_nodes="")

            if check and os.path.exists("./images/tennis_in_crowd.jpg"):
                # Result
                input_image = _read_imgfile("./images/tennis_in_crowd.jpg", width, height)
                input_image = np.array(input_image, dtype=np.float32)
                input_image = input_image.reshape(1, height, width, 3)

                heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = sess.run(
                    outputs,
                    feed_dict={image_ph: input_image}
                )

                print("Test image stats")
                print(input_image)
                print(input_image.shape)
                print(np.mean(input_image))

                heatmaps_result = heatmaps_result[0]

                print("Heatmaps")
                print(heatmaps_result[0:1, 0:1, :])
                print(heatmaps_result.shape)
                print(np.mean(heatmaps_result))
