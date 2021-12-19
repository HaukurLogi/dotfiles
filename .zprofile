# Automatically login to X on tty1
if [ -z "$DISPLAY" ] && [ -n "$XDG_VTNR" ] && [ "$XDG_VTNR" -eq 1 ]; then
    # exec startx -- vt1 &> /dev/null
    exec startx &> /dev/null
fi

