#!/bin/bash
#青龙日志清理
#30 4 * * * clear.sh
#new Env('青龙日志清理');
#

echo “开始清理日志”
find ../log -mtime +1 -name “*.log” -exec rm -rf {} \;
echo “清理日志完成”;