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
import struct

import logging

"""
| ===================================================================
| Constants definition
| ===================================================================
"""
ERROR_FLAG = -1

MAX_MSG_LEN = 65535

SRV_ID = 65535

MESSAGE_TYPES = {"OK": 1, "ERRO": 2, "OI": 3, "FLW": 4, "MSG": 5, "CREQ": 6, "CLIST": 7}

SENDER_RANGE_MIN = 1
SENDER_RANGE_MAX = 4095
VIEWER_RANGE_MIN = 4096
VIEWER_RANGE_MAX = 8191

MAX_CLIENTS = VIEWER_RANGE_MAX - VIEWER_RANGE_MIN + SENDER_RANGE_MAX - SENDER_RANGE_MIN

HEADER_FORMAT = "!HHHH"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

"""
| ===================================================================
| deliver_message: sends a message to a defined host
| ===================================================================
"""

def deliver_message(to_sock, message_type, from_id, to_id, seq_number, message_len=None, message=None):
    logger = logging.getLogger(__name__)
    header = struct.pack(HEADER_FORMAT, message_type, from_id, to_id, seq_number)

    # 5 tries to deliver the message
    for i in range(5):
        try:
            if message_type == MESSAGE_TYPES["MSG"] and message_len:
                to_sock.send(header + struct.pack("!H", message_len) + message)
            elif message_type == MESSAGE_TYPES["CLIST"]:
                to_sock.send(header + struct.pack("!H", message_len), message)
            else:
                to_sock.send(header)

            if message_type != MESSAGE_TYPES["OI"] and message_type != MESSAGE_TYPES["OK"] \
                    and message_type != MESSAGE_TYPES["ERRO"]:
                answer = struct.unpack(HEADER_FORMAT, to_sock.recv(HEADER_SIZE))[0]
                if answer == MESSAGE_TYPES["OK"]:
                    break
                elif answer == MESSAGE_TYPES["ERRO"]:
                    logger.warning("Fail to deliver message")
                    break
            else:
                break
        except:  # TODO better error handling
            pass
