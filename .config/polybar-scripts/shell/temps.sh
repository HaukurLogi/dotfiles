#!/bin/sh

CPU_SENSOR_NAME="Tctl"
GPU_SENSOR_NAME="edge"

CPU_COMMAND=$(sensors | grep $CPU_SENSOR_NAME | tr -d '+' | awk {'print $2'})
GPU_COMMAND=$(sensors | grep $GPU_SENSOR_NAME | tr -d '+' | awk {'print $2'})

if echo $CPU_COMMAND > /dev/null && echo $GPU_COMMAND > /dev/null; then 
  printf "`echo "CPU-TEM: "``echo $CPU_COMMAND`  `echo "GPU-TEM: "` `echo $GPU_COMMAND`"
fi 

