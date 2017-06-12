#!/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2017 
Gabriel Pacheco     <gabriel.pacheco@dcc.ufmg.br> 
Guilherme Sousa     <gadsousa@gmail.com>
Joao Paulo Bastos   <joaopaulosr95@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

==> Gabriel de Oliveira Campos Pacheco  <gabriel.pacheco@dcc.ufmg.br>   2013062898
==> Guilherme Augusto de Sousa          <gadsousa@gmail.com>            2013062944
==> Joao Paulo Sacchetto Ribeiro Bastos <joaopaulosr95@gmail.com>       2013073440
==> Trabalho pratico 2
==> 19-06-2017
"""
import logging
from ..utils import clientutils

# Logging setup
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s]%(message)s")

if __name__ == "__main__":

    logger = logging.getLogger(__name__)

    # get optional parameters
    opt = clientutils.process_opt()

    if opt.sender:
        # connection parameters
        host, port = opt.sender[0].split(':')

        # this sender is attached to a viewer
        if len(opt.sender) > 1:
            viewer_id = opt.sender[1]
            clientutils.sender(host, int(port), int(viewer_id))

        else:
            clientutils.sender(host, int(port))

    elif opt.viewer:
        # connection parameters
        host, port = opt.viewer[0].split(':')

        clientutils.viewer(host, int(port))
