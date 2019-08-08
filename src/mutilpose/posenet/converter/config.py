import yaml
import os

BASE_DIR = os.path.dirname(__file__)


def load_config(config_name='config.yaml'):
    cfg_f = open(os.path.join(BASE_DIR, config_name), "r+")
    cfg = yaml.load(cfg_f)
    return cfg
