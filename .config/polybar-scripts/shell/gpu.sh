#!/bin/sh

GPU_FILE=/sys/class/drm/card1/device/gpu_busy_percent

if test -f $GPU_FILE; then
  printf "`cat $GPU_FILE``echo "%%"`"
fi
