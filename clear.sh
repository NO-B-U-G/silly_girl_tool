#!/bin/bash
#青龙日志清理
#30 4 * * * clear.sh
#new Env('青龙日志清理');
#

echo “开始清理日志”
find /ql/data/log -mtime +1 -name “*.log” -exec rm -rf {} \;
#!/usr/bin/env bash
find /ql/data/log -maxdepth 3 -type d -print -exec rmdir {} 2>/dev/null ;
echo “清理日志完成”;