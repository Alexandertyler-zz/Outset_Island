"Vimrc file for Alex Tyler

"In case it's a systemwide vimrc
"set nocompatible
filetype off

"Launch vundle
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

"Let Vundle manage itself
Plugin 'VundleVim/Vundle.vim'

"Tools
"Plugin 'Valloric/YouCompleteMe'
Plugin 'bkad/CamelCaseMotion'
Plugin 'tpope/vim-fugitive'
Plugin 'scrooloose/syntastic'

"Customizations
Plugin 'bling/vim-airline'
Plugin 'bling/vim-bufferline'
Plugin 'mhinz/vim-signify'

"Colorschemes
Plugin 'morhetz/gruvbox'
Plugin 'altercation/vim-colors-solarized'

"Js
Plugin 'ternjs/tern_for_vim'
Plugin 'jelera/vim-javascript-syntax'

"Html
Plugin 'tpope/vim-surround'

Plugin 'kien/rainbow_parentheses.vim'
augroup RainbowParentheses
    au VimEnter * RainbowParenthesesToggle
    au Syntax * RainbowParenthesesLoadRound
    au Syntax * RainbowParenthesesLoadSquare
    au Syntax * RainbowParenthesesLoadBraces
augroup END

call vundle#end()
filetype plugin indent on

"Set utf8 as standard encoding and en_US as the standard language
set encoding=utf-8
set fileencoding=utf-8

"Set folding for code
set foldenable
set foldmethod=indent
set foldlevelstart=99

"Always show current position
set ruler
set timeoutlen=500

"Height of the command bar
set cmdheight=2

"A buffer becomes hidden when it is abandoned
set hid

"Configure backspace so it acts as it should act
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

"Searching
"Ignore case when searching
set ignorecase
"When searching try to be smart about cases 
set smartcase
"Highlight search results
set hlsearch
"Makes search act like search in modern browsers
set incsearch

"Don't redraw while executing macros (good performance config)
set lazyredraw

"For regular expressions turn magic on
set magic

"Show matching brackets when text indicator is over them
set showmatch
" How many tenths of a second to blink when matching brackets
set mat=2

"Sounds
"No annoying sound on errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Colors and Fonts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Terminal color
set t_Co=256

"Enable syntax highlighting
syntax enable

set background=dark
colorscheme gruvbox

"gruvbox
" let g:gruvbox_contrast_dark="medium"
" let g:gruvbox_contrast_light="medium"

"solarized
"let g:solarized_visibility="high"
"let g:solarized_contrast="high"
"let g:solarized_termcolors=256

"vim-airline configs
let g:airline_powerline_fonts = 1
let g:AirlineTheme="luna"


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Files, backups and undo
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Turn backup off, since most stuff is in SVN, git et.c anyway...
set nobackup
set nowb
set noswapfile

augroup cprog
  autocmd!
  autocmd BufNewFile,BufRead *.c,*.cpp,*.h	set formatoptions=croql
  autocmd BufNewFile,BufRead *.c,*.cpp,*.h	set comments=sr:/*,mb:*,ex:*/
  autocmd BufNewFile,BufRead *.c,*.cpp,*.h	set softtabstop=8
  autocmd BufNewFile,BufRead *.c,*.cpp,*.h	set cino=':0,>2s,n0,e0,p2s,(1s,t0,=2s'
augroup END


augroup pythonprog
    autocmd!
    autocmd BufNewFile,BufRead *.py setlocal expandtab
    autocmd BufNewFile,BufRead *.py set tabstop=4
    autocmd BufNewFile,BufRead *.py set shiftwidth=4
    autocmd BufNewFile,BufRead *.py set softtabstop=4
augroup END

augroup jsprog
    autocmd!
    autocmd BufNewFile,BufRead *.js setlocal expandtab
    autocmd BufNewFile,BufRead *.js setlocal tabstop=2
    autocmd BufNewFile,BufRead *.js setlocal shiftwidth=2
    autocmd BufNewFile,BufRead *.js setlocal softtabstop=2
augroup END

augroup htmlprog
    autocmd!
    autocmd BufNewFile,BufRead *.html setlocal expandtab
    autocmd BufNewFile,BufRead *.html setlocal tabstop=2
    autocmd BufNewFile,BufRead *.html setlocal shiftwidth=2
    autocmd BufNewFile,BufRead *.html setlocal softtabstop=2
augroup END


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Text, tab and indent related
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Set linenumbers
set nu

"Yank lines to OS X clipboard
set clipboard=unnamed
noremap y "+y
noremap yy "+yy
noremap p "+p

"Preserve indentation when pasting from OS X
noremap <leader>p :set paste<CR>:put *<CR>:set nopaste<CR>

"Return key clears search highlighting
nmap <CR> :nohlsearch<CR>
autocmd BufReadPost quickfix nmap <buffer> <CR> <CR>

"Linebreak on 500 characters
set lbr
set tw=500

"Auto indent
set ai
"Smart indent
set si
"Wrap lines
set wrap

""""""""""""""""""""
"Control Remappings"
""""""""""""""""""""

"Map mouse controls if not using neovim
if !has('nvim')
    set mouse=a
    set ttymouse=xterm2
endif

"Aliases
:command WQ wq
:command Wq wq
:command W w
:command Q q

set listchars=tab:∫-
set list
set shiftwidth=4

"Change the window resizing to +,-
if bufwinnr(1)
    map + <C-w>+
    map - <C-w>-
    map [ <C-w><
    map ] <C-w>>
endif

"add buffer close command
command Bc bp\|bd \#

"""""""""""""""""""""""""""""
" Neovim Control Remappings "
"""""""""""""""""""""""""""""
if has('nvim')
    :tnoremap <C-w>h <C-\><C-n><C-w>h
    :tnoremap <C-w>j <C-\><C-n><C-w>j
    :tnoremap <C-w>k <C-\><C-n><C-w>k
    :tnoremap <C-w>l <C-\><C-n><C-w>l
    :tnoremap <C-w><Esc> <C-\><C-n> 
endif
