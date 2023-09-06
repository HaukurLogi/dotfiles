#!/bin/sh

python $HOME/python/app-command.py --runningcmd 'nvidia-settings -a "DigitalVibrance=716"' --stoppedcmd 'nvidia-settings -a "DigitalVibrance=0"' --app 'csgo_linux64'
