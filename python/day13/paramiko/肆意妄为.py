#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import paramiko
import sys
import os
import socket
import select
import getpass
from paramiko.py3compat import u

tran = paramiko.Transport(('127.0.0.1', 22,))
tran.start_client()
tran.auth_password('lianliang', 'woyaojueqi')

# 打开一个通道
chan = tran.open_session()
# 获取一个终端
chan.get_pty()
# 激活器
chan.invoke_shell()

while True:
    # 监视用户输入和服务器返回数据
    # sys.stdin 处理用户输入
    # chan 是之前创建的通道，用于接收服务器返回信息
    readable, writeable, error = select.select([chan, sys.stdin, ],[],[],1)
    if chan in readable:
        try:
            x = u(chan.recv(1024))
            if len(x) == 0:
                print('\r\n*** EOF\r\n')
                break
            sys.stdout.write(x)
            sys.stdout.flush()
        except socket.timeout:
            pass
    if sys.stdin in readable:
        inp = sys.stdin.readline()
        chan.sendall(inp)

chan.close()
tran.close()