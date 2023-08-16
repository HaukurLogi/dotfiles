#!/bin/sh
xrandr --output DP-0 --primary --mode 1920x1080 --rotate normal --rate 240.00 
xrandr --output HDMI-0 --mode 1280x720 --left-of DP-4 --pos 0x0 --rotate left --rate 60.00
xrandr --output DP-0 --mode 2560x1440 --rate 144.00 --pos 0x0 --rotate normal
