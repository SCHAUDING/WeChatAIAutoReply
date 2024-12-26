from wxauto import WeChat
import requests
import json


API_KEY = "YOUR API_KEY"
SECRET_KEY = "YOUR SECRET_KEY"
 
def aiautoreply(content):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-char-8k?access_token=" + get_access_token()
 
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    # print(payload)
    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(response['result'])
    return response['result']
 
def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    # print(str(requests.post(url, params=params).json().get("access_token")))
    return str(requests.post(url, params=params).json().get("access_token"))
 

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
        
        # AI回复
        for msg in one_msgs:
            if msg.type == 'friend':
                sender = msg.sender 
                print(f'{sender.rjust(20)}：{msg.content}')
                reply=str(aiautoreply(msg.content))
                chat.SendMsg(reply) 
