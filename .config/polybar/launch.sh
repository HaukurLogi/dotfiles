#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch the bars
barname=top
if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m nice -n4 polybar --reload $barname &
  done
else
  nice -n4 polybar --reload $barname &
fi

echo "Bars launched..."
