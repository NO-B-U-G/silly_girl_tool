#!/bin/bash
#重启qq
#1 1 1 1 1 qq_start.py
#new Env('重启qq');
#

import os
from time import sleep

#const $ = new Env("qq机器人启动");

if __name__ == '__main__':
    print('启动中')
    print('杀死进程')
    os.system('nsenter --mount=/host/proc/1/ns/mnt bash -c "killall /usr/qq/go-cqhttp"')
    sleep(5)
    os.system('nsenter --mount=/host/proc/1/ns/mnt bash -c "cd /usr/qq && ./go-cqhttp -d"')
    sleep(5)
    print('命令执行完成')