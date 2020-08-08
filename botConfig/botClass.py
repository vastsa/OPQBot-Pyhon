import json

import requests
from .configInfo import *

"""
By : Lan
Website : 
"""

# 群组消息接受类
class GroupMess:
    def __init__(self, message):
        self.FromQQG = message['FromGroupId']  # 来源QQ群
        self.QQGName = message['FromGroupName']  # 来源QQ群昵称
        self.FromQQ = message['FromUserId']  # 来源QQ
        self.FromQQName = message['FromNickName']  # 来源QQ名称
        self.Content = message['Content']  # 消息内容
        self.Msgtime = message['MsgTime']  # 消息时间


# 私发消息接受类
class PrivateMess:
    def __init__(self, message):
        self.FromQQ = message['ToUin']  # 来源QQ号
        self.ToQQ = message['FromUin']  # 目标QQ号
        self.Content = message['Content']  # 消息内容
        self.MsgType = message['MsgType']  # 消息类型


# 发送消息类
class SendMessage:
    def __init__(self, toUser=0, sendToType=0, sendMsgType='', groupId=0, content='', atUser=0, voiceUrl='', picUrl='',
                 picBase64Buf='', voiceBase64Buf=''):
        self.data = {
            "toUser": toUser,  # 欲发给的对象 群或QQ好友或私聊对象
            "sendToType": sendToType,  # 发送消息对象的类型 1好友 2群3私聊
            "sendMsgType": sendMsgType,  # 欲发送消息的类型 TextMsg、PicMsg、VoiceMsg
            "content": content,  # 发送的文本内容
            "groupid": groupId,  # 发送私聊消息是 在此传入群ID 其他情况为0
            "atUser": atUser,  # At用户 传入用户的QQ号 其他情况为0
            "picUrl": picUrl,  # 发送图片的网络地址
            "picBase64Buf": picBase64Buf,  # 发本地送图片的buf 转 bas64 编码
            "voiceUrl": voiceUrl,  # 发送语音的网络地址
            "voiceBase64Buf": voiceBase64Buf,  # 发本地送语音的buf 转 bas64 编码
            "fileMd5": ""
        }

    '''
    发送图片消息需要有：toUser sendToType sendMsgType picUrl
    '''

    def send(self):
        print(self.data)
        requests.post(url=f'{webapi}/v1/LuaApiCaller?qq={robotQQ}&funcname=SendMsg&timeout=10',
                      data=json.dumps(self.data))
        return 200