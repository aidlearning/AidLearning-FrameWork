package com.aidlux.usbcamera;

import android.content.Context;
import android.os.Environment;
import android.util.Log;

import org.acra.ReportField;
import org.acra.data.CrashReportData;
import org.acra.sender.ReportSender;
import org.acra.sender.ReportSenderException;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class AcraFileSender implements ReportSender {
    @Override
    public void send(Context context, CrashReportData report) throws ReportSenderException {
        String error_log = "";
        error_log += report.getString(ReportField.LOGCAT);
//        final String storagePath = context.getExternalFilesDir(null).getAbsolutePath() + File.separator + "USBCamera";
        final String storagePath = Environment.getExternalStorageDirectory().getAbsolutePath() + File.separator + "USBCamera";
        final String crashFileName = "CrashReport.txt";
        final File storageDir = new File(storagePath);
        if (!storageDir.exists()) {
            storageDir.mkdir();
        }
        String crashFilePath = storagePath + File.separator + crashFileName;

        try {
            File file = new File(crashFilePath);
            FileOutputStream out = new FileOutputStream(file);
            OutputStreamWriter writer = new OutputStreamWriter(out);

            writer.append(error_log);
            writer.close();

            out.flush();
            out.close();

            Log.i("Acra", "Crash log saved.");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
