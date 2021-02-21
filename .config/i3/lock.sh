#!/bin/bash
# Let's first assume we have the i3lock-color fork.
B='#00000000'  # blank
C='#ffffff22'  # clear ish
D=$C  # default
T='#ffffffff'  # text
W='#ff0000ff'  # wrong
R='#00ff00ff'  # right
V='#bb00bbbb'  # verifying

/usr/bin/i3lock \
--insidevercolor=$C   \
--ringvercolor=$V     \
\
--insidewrongcolor=$C \
--ringwrongcolor=$W   \
\
--insidecolor=$B      \
--ringcolor=$D        \
--linecolor=$B        \
--separatorcolor=$D   \
\
--verifcolor=$T       \
--wrongcolor=$T       \
--timecolor=$T        \
--datecolor=$T        \
--layoutcolor=$B      \
--keyhlcolor=$R       \
--bshlcolor=$W        \
\
--screen 1            \
--blur 5              \
--clock               \
--indicator           \
--timestr="%H:%M:%S"  \
--datestr="%A, %m %Y" \
--keylayout 0

# Check return code
if [ ! $? -eq "0" ]; then
    # Return code is not zero. This likely means that
    # we don't have i3lock-color. Let's try without
    # the i3lock-color specific options.
    RES=$(xdpyinfo | grep dimensions | \
        sed -r 's/^[^0-9]*([0-9]+x[0-9]+).*$/\1/')
    IMAGE=$(mktemp).png

    /usr/bin/ffmpeg \
        -probesize 100M -thread_queue_size 32 -f x11grab -video_size $RES \
        -loglevel quiet -y -i $DISPLAY -filter_complex "boxblur=8:8" \
        -vframes 1 $IMAGE

    echo "locked;$(date -u +%s.%N)" >> /tmp/time_locked
    # Do the actual locking
    /usr/bin/i3lock -n -i "$IMAGE"
    echo "unlocked;$(date -u +%s.%N)" >> /tmp/time_locked

    # Delete image after use
    rm $IMAGE
fi
