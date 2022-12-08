# clash启动
#cron:11 11 11 11


import os
from time import sleep

#const $ = new Env("启动clash");

if __name__ == '__main__':
    print('启动中')
    os.system('cd /root/clash && ./clash -d .')
    sleep(8)
    print('命令执行完成')