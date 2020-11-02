# vim: noet
# -- Path --
export PATH="$HOME/scripts:$HOME/.local/bin:$HOME/bin:/usr/local/bin:$PATH"

# -- XDG Directories --
export XDG_CONFIG_HOME="$HOME/.config"

# -- Applications --
export EDITOR="nvim"
export VISUAL="nvim"
export TERMINAL="alacritty"

# -- Settings --
# QT
export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb

# Compilation
export RUSTFLAGS="-C target-cpu=native"

# Enable Firefox WebRender
export MOZ_ACCELERATED=1
export MOZ_WEBRENDER=1

# Opt out of Microsoft's telemetry
DOTNET_CLI_TELEMETRY_OPTOUT=1

# Always display Rust backtrace on panic
RUST_BACKTRACE=full

# ls / completion colors --
export LS_COLORS='ow=36:di=34:fi=32:ex=31:ln=35:'
export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=2"

# -- History --
export HISTFILE="$HOME/.zsh_history"
export SAVEHIST=1000000
export HISTSIZE=1000000