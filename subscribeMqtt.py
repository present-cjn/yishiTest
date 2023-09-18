# -*- coding: utf-8 -*-
"""
Time:     2023/9/18 9:19
Author:   cjn
Version:  1.0.0
File:     subscribeMqtt.py
Describe: 
"""
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # 连接成功后订阅主题
    client.subscribe("subsys_mqtt_heartbeat_topic")
    client.subscribe("subsys_mqtt_heartbeat_topic")

def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())

# 创建 MQTT 客户端
client = mqtt.Client()

# 设置连接回调函数
client.on_connect = on_connect

# 设置消息接收回调函数
client.on_message = on_message

# 设置 MQTT 服务器地址和端口
broker_address = "192.168.1.150"
broker_port = 1883

# 连接到 MQTT 服务器
client.connect(broker_address, broker_port, 60)

# 开始循环处理网络流量，保持与 MQTT 服务器的连接
client.loop_forever()