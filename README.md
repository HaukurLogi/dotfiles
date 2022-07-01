# My dotfiles

Example of what it looks like. 

![demo](https://github.com/HaukurLogi/dotfiles/blob/master/images/Example.png)

### Disclaimer

I'm changing this constantly, so if you install this beware that it may not look like it completely.

### Install

```
curl -Lks https://raw.githubusercontent.com/HaukurLogi/dotfiles/master/.config/install.sh | bash
```

### Command to push

```
config push https://<Token>@github.com/HaukurLogi/dotfiles.git
```

### Oh-my-zsh

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

### Zsh-autosuggestions

```
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

### Zsh-syntax-highlighting

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```
