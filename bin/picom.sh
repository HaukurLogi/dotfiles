#!/bin/sh 

if hostnamectl | grep 'arm64'; then
    picom --backend xrender
else
    picom
fi
