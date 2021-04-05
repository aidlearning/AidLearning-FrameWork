#!/bin/bash
#set -ex
#source ~/.bashrc  # ADD THIS LINE
#export PATH=$PATH:/usr/local/go/bin
######################################
python2 /root/.startx >/dev/null 2>&1 &
python2 /root/.startssh >/dev/null 2>&1 &
python2 /home/.remi/editor/.toucheditor >/dev/null 2>&1 &
cd /;filebrowser -a 0.0.0.0 -r / >/dev/null 2>&1 &
cd /;./.cosv --port 8008 --auth none --locale zh-cn >/dev/null 2>&1 &
cd /home;jupyter notebook --allow-root >/dev/null 2>&1 &
# cd /root/OS.js;npm run serve >/dev/null 2>&1 &
