#!/bin/bash
#重启傻妞
#1 1 1 1 1 silly_start.py
#new Env('重启傻妞');
#

import os
from time import sleep

#const $ = new Env("重启傻妞");


if __name__ == '__main__':
    print('重启傻妞')
    print('停止傻妞')
    os.system('nsenter --mount=/host/proc/1/ns/mnt bash -c "ps -ef | grep sillyGirl | grep -v grep | awk '{print $2}' | xargs kill"')
    sleep(5)
    print('启动傻妞')
    os.system('nsenter --mount=/host/proc/1/ns/mnt bash -c "cd /usr/local/sillyGirl && ./sillyGirl -d"')
    sleep(5)
    print('命令执行完成')

