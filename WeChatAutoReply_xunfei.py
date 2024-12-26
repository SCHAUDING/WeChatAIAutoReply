import traceback
from websocket import WebSocketException
from wxauto import WeChat
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import re

def aiautoreply(text):
    #星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_URL = ''
    #星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
    SPARKAI_APP_ID = ''
    SPARKAI_API_SECRET = ''
    SPARKAI_API_KEY = ''
    #星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_DOMAIN = ''

    spark = ChatSparkLLM(
    spark_api_url=SPARKAI_URL,
    spark_app_id=SPARKAI_APP_ID,
    spark_api_key=SPARKAI_API_KEY,
    spark_api_secret=SPARKAI_API_SECRET,
    spark_llm_domain=SPARKAI_DOMAIN,
    streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content=text
    )]
    handler = ChunkPrintHandler()
    try:
        # 调用大模型接口生成回复
        reply = spark.generate([messages], callbacks=[handler])
        return reply

    except WebSocketException as ws_error:
        print("WebSocket 连接失败，请检查网络或服务地址。")
        return "网络连接失败，请稍后重试。"

    except Exception as e:
        # 捕获错误并打印详细堆栈信息
        print("发生错误:", traceback.format_exc())
        error_message = str(e)
        if "Error Code: 10013" in error_message:
            return "检测到违禁内容，无法生成回复。"
        else:
            return "发生未知错误，请稍后重试。"

def get_info(reply_text):
    # 使用正则表达式提取content中的内容
    content = re.search(r"content='([^']+)'", reply_text)

    # 如果匹配成功，返回匹配到的内容
    if content: 
        return content.group(1)  # 输出提取到的内容
    else:
        return "当前内容无法进行回复,请更换内容后重试"


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
                reply="【自动回复】"+get_info(str(aiautoreply(msg.content)))
                chat.SendMsg(reply)  