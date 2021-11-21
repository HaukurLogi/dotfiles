
#!/bin/sh

eval $(gnome-keyring-daemon --start)
export SSH_AUTH_SOCK
xset r rate 250 30
exec i3
