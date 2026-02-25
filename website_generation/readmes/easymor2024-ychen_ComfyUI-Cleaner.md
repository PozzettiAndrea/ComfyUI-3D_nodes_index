# ComfyUI-Cleaner

ComfyUI plugins of File Cleaning

基于容器化部署comfyui，输出文件comfyui/output/ 下会日积月累文件，由此开发的自动清理输出文件的插件；

支持多目录清理。

部署方式:

## 假设您的源码文件地址是：comfyui/

cd comfyui/custom_nodes

## 拉取代码

git clone https://github.com/easymor2024-ychen/ComfyUI-Cleaner.git

## 执行依赖下载

pip install -r requirements.txt

## 重启comfyui

```txt
文件放入comfyui/custom_nodes/
可通过环境变量配置清理参数：
    CLEANUP_DIRECTORIES：监控目录，逗号分隔
    RETENTION_DAYS：保留时间（支持 s/m/h/d 单位，如 "7d"）
    MAX_FILES_PER_DIR：最大文件数
    MAX_DISK_SIZE_MB：最大磁盘占用 (MB)
    SCAN_INTERVAL：清理扫描间隔 (秒)
    MONITOR_INTERVAL：线程监控间隔 (秒)，默认 300
    CPU_THRESHOLD: 低于多少利用率执行 80%
    STATE_FILE: 清理-扫描记录文件 默认 /tmp/cleanup_daemon_state.json
启动 ComfyUI 时会自动加载并启动清理程序，无需额外操作
```
