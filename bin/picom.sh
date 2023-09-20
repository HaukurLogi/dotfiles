#!/bin/sh 

if hostnamectl | grep 'x86-64'; then
    picom
fi

