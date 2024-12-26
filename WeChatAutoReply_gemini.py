from wxauto import WeChat
import json
import requests

def aiautoreply(text):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=你的APIKEY'
    headers = {'Content-Type': 'application/json'}
    data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': text
                        }
                    ]
                }
            ]
        }
 
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['candidates'][0]['content']['parts'][0]['text']


wx = WeChat()

# 首先设置一个监听列表，列表元素为指定好友（或群聊）的昵称
listen_list = [
    '张三',
    '李四'
]

# 然后调用`AddListenChat`方法添加监听对象，其中可选参数`savepic`为是否保存新消息图片
for i in listen_list:
    wx.AddListenChat(who=i)

while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        one_msgs = msgs.get(chat)   # 获取消息内容
        
        # 回复收到
        for msg in one_msgs:
            if msg.type == 'friend':
                sender = msg.sender 
                print(f'{sender.rjust(20)}：{msg.content}')
                reply=str(aiautoreply(msg.content))
                chat.SendMsg(reply) 
