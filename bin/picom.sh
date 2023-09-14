#!/bin/sh 

if hostnamectl | grep 'x86_64'; then
    picom
fi

