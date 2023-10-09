#!/bin/sh

printf "`echo "CPU-TEM: "``sensors | grep "Tctl" | tr -d '+' | awk '{print $2}'`  `echo "GPU-TEM: "` `sensors | grep "edge" | tr -d '+' | awk '{print $2}'`"
