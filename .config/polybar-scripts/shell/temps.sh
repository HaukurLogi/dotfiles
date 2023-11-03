#!/bin/sh

CPU_SENSOR_NAME="Tctl"
GPU_SENSOR_NAME="edge"

CPU_COMMAND=$(sensors | grep $CPU_SENSOR_NAME | tr -d '+' | awk {'print $2'})
GPU_COMMAND=$(sensors | grep $GPU_SENSOR_NAME | tr -d '+' | awk {'print $2'})

if echo $COMMAND1 && echo $COMMAND2; then 
    printf "`echo "CPU-TEM: "``$COMMAND1`  `echo "GPU-TEM: "` `$COMMAND2`"
fi 

