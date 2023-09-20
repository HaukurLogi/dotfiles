#!/bin/sh

sensors | grep "Tccd2" | tr -d '+' | awk '{print $2}'
