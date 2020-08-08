# coding=utf-8
# By :Lan
# Blog :https://www.lanol.cn
import logging
import time
import socketio
from botConfig.botClass import *
from botConfig.configInfo import *

sio = socketio.Client()


def beat():
    while True:
        sio.emit('GetWebConn', robotQQ)
        time.sleep(60)


@sio.event
def connect():
    print('connected to server')
    sio.emit('GetWebConn', robotQQ)  # 取得当前已经登录的QQ链接
    beat()  # 心跳包，保持对服务器的连接


@sio.on('OnGroupMsgs')
def OnGroupMsgs(message):
    """ 监听群组消息"""
    data = GroupMess(message['CurrentPacket']['Data'])
    print(data)
    return


@sio.on('OnFriendMsgs')
def OnFriendMsgs(message):
    """ 监听好友消息 """
    data = PrivateMess(message['CurrentPacket']['Data'])
    print(data)
    return


@sio.on('OnEvents')
def OnEvents(message):
    """ 监听相关事件"""
    print(message)


def main():
    try:
        sio.connect(webAPI, transports=['websocket'])
        sio.wait()
    except BaseException as e:
        logging.info(e)
        print(e)


if __name__ == '__main__':
    main()
