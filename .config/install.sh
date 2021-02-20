#!/bin/bash
set -xeo pipefail

git clone --bare https://github.com/HaukurLogi/dotfiles.git $HOME/.dotfiles

function config {
   /usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME $@
}

mkdir -p .dotfiles-backup
config checkout || config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} bash -c 'mkdir -p `dirname .dotfiles-backup/{}` && mv {} .dotfiles-backup/{}'

config config --local status.showUntrackedFiles no
