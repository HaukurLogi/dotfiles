#!/bin/sh

set -ex

if [ "$#" -eq 0 ]; then
    echo "Usage: mpvbg PATH [{w}x{h}+{x}+{y}]"
    exit
fi
[ -f "$1" ] || exit

pkill -9 xwinwrap || true

if [ -n "$2" ]; then
    xwin="xwinwrap -g "$2" -ni -fdt -sh rectangle -un -b -nf -ov -- "
else
    xwin="xwinwrap -ni -fdt -sh rectangle -un -b -nf -ov -fs -- "
fi

# --vo=xv  # less costly but laggy
mpv="mpv -wid WID --no-config --keepaspect=no --loop \
    --no-border --vd-lavc-fast --x11-bypass-compositor=no \
    --gapless-audio=yes --hwdec=auto --really-quiet \
    --name=mpvbg"

$xwin $mpv "$1" 2>&1 &
