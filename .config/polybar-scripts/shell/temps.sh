#!/bin/sh

CPU="Tctl"
GPU="edge"

CPU_COMMAND=$(sensors | grep $CPU | tr -d '+' | awk {'print $2'})
GPU_COMMAND=$(sensors | grep $GPU | tr -d '+' | awk {'print $2'})

if echo $COMMAND1 && echo $COMMAND2
then 
    printf "`echo "CPU-TEM: "``$COMMAND1`  `echo "GPU-TEM: "` `$COMMAND2`"
fi 

