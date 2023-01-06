# go-cqhttp(qq机器人)启动
#cron:11 11 11 11


import os
from time import sleep

#const $ = new Env("qq机器人启动");

if __name__ == '__main__':
    print('启动中')
    print('杀死进程')
    os.system('pkill go-cqhttp')
    sleep(5)
    os.system('cd /root/go-cqhttp && ./go-cqhttp -d')
    sleep(5)
    print('命令执行完成')