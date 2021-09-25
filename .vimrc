" MIT License
" 
" Copyright (c) 2021 Xinas
" 
" Permission is hereby granted, free of charge, to any person obtaining a copy
" of this software and associated documentation files (the "Software"), to deal
" in the Software without restriction, including without limitation the rights
" to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
" copies of the Software, and to permit persons to whom the Software is
" furnished to do so, subject to the following conditions:
" 
" The above copyright notice and this permission notice shall be included in all
" copies or substantial portions of the Software.
" 
" THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
" IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
" FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
" AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
" LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
" OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
" SOFTWARE.

" 
" GENERAL SETTINGS
" 

" Remove VI compatibility mode (redundant)
set nocompatible
" Enable syntax highlighting
syntax on
" Enable automatic filetype detection and indentation
filetype plugin indent on
" Change from tabs to spaces
set tabstop=2 shiftwidth=2 expandtab
" Show line number
set number

" 
" PLUGIN SETTINGS
"

" Autoinstall vim-plug
let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Plugins
call plug#begin('~/.vim/plugged')
  Plug 'arcticicestudio/nord-vim'
  Plug 'preservim/nerdtree'
  Plug 'rust-lang/rust.vim'
call plug#end()

" 
" THEME SETTINGS
"

" Chage color scheme
colorscheme nord

" Display emojis in vim
set encoding=utf-8
set t_Co=256
set termencoding=utf-8

" Change cursor in insert mode
let &t_SI = "\e[6 q"
let &t_EI = "\e[2 q"

" Fix dealy after hitting <Esc> key
set ttimeout
set ttimeoutlen=1
set listchars=tab:>-,trail:~,extends:>,precedes:<,space:.
set ttyfast

" 
" STATUSLINE SETTINGS
"

" Vim current mode config
let g:currentmode={
       \ 'n'  : ' NORMAL ',
       \ 'v'  : ' VISUAL ',
       \ 'V'  : ' V·Line ',
       \ "\<C-V>" : ' V·Block ',
       \ 'i'  : ' INSERT ',
       \ 'R'  : ' R ',
       \ 'Rv' : ' V·Replace ',
       \ 'c'  : ' Command ',
       \}

" Status line always visible
set laststatus=2
" Reset status line (and start with a space)
set statusline=\ 

" [LEFT] Current mode
set statusline+=<<%{toupper(g:currentmode[mode()])}>>
" [LEFT] Git branch
" [LEFT] File name
set statusline+=\ \ %f\ 
" [LEFT] Modified status
set statusline+=%{&modified?'[+]\ ':''}
" [LEFT] Readonly status
let &statusline .= '%{(&readonly || !&modifiable) ? "" : ""}'
" Change alignment
set statusline+=%=
" [RIGHT] Line and column
set statusline+=Ln:%01l,Col:%01v\ \ 
" [RIGHT] Encoding
set statusline+=%{&fileencoding?&fileencoding:&encoding}\ \ 
" [RIGHT] Filetype
set statusline+=%{strlen(&filetype)?&filetype:'Plain\ text'}\ \ 

" 
" NERDTree SETTINGS
"

" Set current directory
autocmd BufEnter * lcd %:p:h
" Start NERDTree and put the cursor back in the other window.
autocmd VimEnter * NERDTree | wincmd p
" Open the existing NERDTree on each new tab.
autocmd BufWinEnter * if getcmdwintype() == '' | silent NERDTreeMirror | endif
" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
" Close the tab if NERDTree is the only window remaining in it.
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

