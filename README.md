# Xinas' dotfiles

![Arch Linux package](https://img.shields.io/archlinux/v/core/x86_64/linux)
![GitHub](https://img.shields.io/github/license/Xinas/dotfiles?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Xinas/dotfiles?style=flat-square)

## Introduction

In order to make these dotfiles, I followed [this](https://www.atlassian.com/git/tutorials/dotfiles) tutorial.

## Installation

```bash
git clone --bare https://github.com/Xinas/dotfiles.git $HOME/.dot
alias dot='/usr/bin/git --git-dir=$HOME/.dot/ --work-tree=$HOME'
dot checkout
```

