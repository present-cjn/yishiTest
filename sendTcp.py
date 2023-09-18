# -*- coding: utf-8 -*-
"""
Time:     2023/9/18 9:18
Author:   cjn
Version:  1.0.0
File:     sendTcp.py
Describe: 
"""
import socket
import json

# TCP服务器的地址和端口
# server_address = ('192.168.3.12', 9528)
server_address = ('192.168.1.150', 9528)
# server_address = ('127.0.0.1', 9528)

# 要发送的数据
data = {"action": "connectMQTT",
        "username": "admin",
        "password": "public",
        "ip": "192.168.1.150",
        "port": "1883",
        "subsys_mqtt_public_topic": "subsys_mqtt_public_topic",
        "subsys_mqtt_subscribe_topic": "subsys_mqtt_subscribe_topic",
        "subsys_mqtt_publish_topic": "subsys_mqtt_publish_topic",
        "subsys_mqtt_heartbeat_topic": "subsys_mqtt_heartbeat_topic"
        }

# 创建TCP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 连接到服务器
    sock.connect(server_address)

    # 将数据序列化为JSON字符串，并编码为字节流
    json_data = json.dumps(data).encode('utf-8')

    # 发送数据
    sock.sendall(json_data)
    sock.shutdown(socket.SHUT_WR)

    # 接收服务器的响应
    response = sock.recv(1024)
    print('Received:', response.decode())

finally:
    # 关闭套接字
    sock.close()
