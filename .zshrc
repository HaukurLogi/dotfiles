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

# Neofetch
if ps -e | grep 'alacritty' | wc -l | grep '1' > /dev/null; then 
    neofetch
fi 

# Generated for envman. Do not edit.
[ -s "$HOME/.config/envman/load.sh" ] && source "$HOME/.config/envman/load.sh"
