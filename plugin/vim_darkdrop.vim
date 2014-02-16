" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! DarkDropFile()
python << endOfPython

from vim_darkdrop import *
DarkDropFile()
endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! DarkDrop call DarkDropFile()
