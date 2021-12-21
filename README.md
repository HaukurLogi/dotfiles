Run the following:
```
curl -Lks https://raw.githubusercontent.com/HaukurLogi/dotfiles/master/.config/install.sh | bash
```
```
config push https://<Token>@github.com/HaukurLogi/dotfiles.git
```

Install oh-my-zsh and plugins:
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
zsh-autosuggestions
```
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
```
zsh-syntax-highlighting
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```
