#!/bin/bash
## 启动宿主机脚本 需要容器能执行宿主机
#1 1 1 1 1 start.py
#new Env('启动宿主机脚本');
#

import os
from time import sleep

#const $ = new Env("启动宿主机脚本");

if __name__ == '__main__':
    print('启动中')
    os.system('nsenter --mount=/host/proc/1/ns/mnt bash -c "cd /usr && sh start.sh"')
    sleep(8)
    print('命令执行完成')