# 智能灌水系统完整项目
**际场地由两台7.5KW 水泵 + 2两台11 KW 水泵组成，外加10个电球阀组成，由电气柜统一控制**
<br> 前端微信小程序发送指令，云端Django后台负责处理信息，并且通过websocket发送指令到电气柜内安放的树莓派内 </br>
<br> 树莓派通过协程解析指令，并通过网线与plc通信，进而控制电气柜 </br>

<img src="./img/示意图.jpg"></img>
<img src="./img/电气柜.jpg">

## Django 后端

<br> 技术栈 Django + DRF + websocket + uwsgi + daphne + nginx + docker + redis </br>
<br>在云服务器中部署docker，再将后台放入创建的容器中 </br>


### Django

<br> 因为主要处理微信小程序的请求，因此仅仅创建一个app Monitor


## 微信小程序
<img src="./img/1.png"><img src="./img/2.png"><img src="./img/2.1.png"><img src="./img/3.png">


## 树莓派

<br> 代码见client


## 使用

### 准备工作
需要一个ubuntu 20服务器

###  安装docker（参考如下博客）
可以在本地安装vm，或者租用云服务器
```
https://blog.csdn.net/u011278722/article/details/137673353
```
### 或者安装docker windows版本<不建议>
<br> 可以安装windows版本，再安装ubuntu

```angular2html
https://blog.csdn.net/HYP_Coder/article/details/141753300
```

### 下载微信小程序开发工具
```angular2html
https://developers.weixin.qq.com/miniprogram/dev/devtools/stable.html
```
### 使用docker 安装redis
在本项目django 中已经配置好,可以自行b站学习redis docker配置

```angular2html
配置redis(docker)
进入配置好的redis
sudo docker exec -it my-redis redis-cli -a your_password
查看docker 网络
sudo docker network inspect django-redis-net
查看log
sudo docker logs my-redis
使用docker网络创建容器
sudo docker run -d   --name my-redis   --network django-redis-net   -p 6379:6379   swr.cn-east-3.myhuaweicloud.com/library/redis:latest   redis-server --requirepass "your_password" --appendonly yes
创建网络
docker network create django-redis-net
下载华为云的redis docker镜像
sudo docker pull swr.cn-east-3.myhuaweicloud.com/library/redis:latest
重启docker
 sudo systemctl restart docker
关闭 docker
sudo systemctl daemon-reload
```

### 在docker中配置python环境
```
pip install  -r requirements.txt
```

### 使用前须知
<br> redis 启动
<br> daphne 启动
<br> uwsgi 启动
<br> nginx 启动
<br> docker 将相应端口映射到操作系统对应端口

### 运行本程序云端
<br > 相关指令见django.docx
<br>nginx 启动

```angular2html

```
websocket 服务器启动
```angular2html
daphne -b 0.0.0.0 -p 5015 Aurage.asgi:application
```
django 启动， 在根目录
```angular2html
uwsgi --ini scripts/uwsgi.ini
```
