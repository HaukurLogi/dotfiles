#!/bin/bash
arg="${1:-}"
case "$arg" in
  --speakers)
    CARD="Speakers"
    SINK="alsa_output.usb-Bose_Corporation_Bose_USB_Audio-00.analog-surround-51"
    pacmd set-default-sink "$SINK"
    pacmd list-sink-inputs | grep index | while read line; do
    pacmd move-sink-input `echo $line | cut -f2 -d' '` "$SINK"
    done
    ;;
  --headphones)
    CARD="Headphones"
    SINK="alsa_output.pci-0000_00_1b.0.analog-stereo"
    pacmd set-default-sink "$SINK"
    pacmd list-sink-inputs | grep index | while read line; do
    pacmd move-sink-input `echo $line | cut -f2 -d' '` "$SINK"
    done
    ;;
    *)
echo "Headphones"
    ;;
esac
