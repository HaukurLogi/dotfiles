#!/bin/sh
# Uses xwinwrap to display given animated .gif in the center of the screen

if [ $# -ne 1 ]; then
echo 1>&2 Usage: $0 image.gif
exit 1
fi

# Get screen resolution
SCRH=`xrandr | awk '/current/ { print $8 }'`
SCRW=`xrandr | awk '/current/ { print $10 }' | sed 's/,//'`

# Get gif resolution
IMGHW=`gifsicle --info $1 | awk '/logical/ { print $3 }'`
IMGH=${IMGHW%x*}
IMGW=${IMGHW#*x}

# Calculate position
POSH=$((($SCRH/2)-($IMGH/2)))
POSW=$((($SCRW/2)-($IMGW/2)))

xwinwrap -g ${IMGHW}+${POSH}+${POSW} -ov -ni -s -nf -b -sh circle -- mpv -wid WID --hwdec=auto --x11-bypass-compositor=no --geometry=${IMGHW}+${POSH}+${POSW} --loop --really-quiet --vd-lavc-fast --no-border $1 2>&1 &

exit 0
