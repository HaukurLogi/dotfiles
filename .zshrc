# Path
export PATH=$HOME/.local/bin:$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Theme 
ZSH_THEME="fwalch"

# Plugins 
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

# Oh-my-zsh
source $ZSH/oh-my-zsh.sh

# Editor
export EDITOR='nvim'

# Locale
export LANG=en_US.UTF-8

# Aliases 
source "$HOME/.config/zsh/alias.zsh"

# Colorscripts only appear on Linux
if echo $OSTYPE | grep 'linux' >/dev/null; then
	colorscript -r
else
	eval $(/opt/homebrew/bin/brew shellenv)
fi

# Pfetch
pfetch

# Generated for envman. Do not edit.
[ -s "$HOME/.config/envman/load.sh" ] && source "$HOME/.config/envman/load.sh"
