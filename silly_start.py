# 傻妞启动
#cron:11 11 11 11


import os
from time import sleep

#const $ = new Env("启动傻妞");

if __name__ == '__main__':
    print('启动中')
    os.system('cd /usr/local/sillyGirl && ./sillyGirl -d')
    sleep(8)
    print('命令执行完成')