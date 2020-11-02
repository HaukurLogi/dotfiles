# Load aliases
source "$HOME/.config/zsh/alias.zsh"

# Load zsh options
source "$HOME/.config/zsh/setopt.zsh"

# Completion and ls colors
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*:*:*:*:*' menu yes select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z-_}={A-Za-z_-}' 'r:|=*' 'l:|=* r:|=*'
zstyle ':completion:*' menu select

# Autoload functions
autoload -U compinit && compinit
autoload -U colors && colors
autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search

zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

# Load keybindings
source "$HOME/.config/zsh/keybindings.zsh"

# Environment variables for gpg
export GPG_TTY="$(tty)"
unset SSH_AGENT_PID
export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)
gpg-connect-agent updatestartuptty /bye > /dev/null

# Autosuggestions. Clone 'zsh-autosuggestions' from:
# https://github.com/zsh-users/zsh-autosuggestions.git
source "$HOME/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh"
# Syntax highlighting. Clone 'zsh-syntax-highlighting' from:
# https://github.com/zsh-users/zsh-syntax-highlighting.git
source "$HOME/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"

# Load prompt
source "$HOME/.config/zsh/ps1.zsh"
