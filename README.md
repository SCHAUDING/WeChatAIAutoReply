# 微信AI自动回复
## 简要说明
依靠[wxauto](https://github.com/cluic/wxauto)实现的微信AI自动回复程序，目前制作了百度、讯飞、Gemini三个平台的AI自动回复程序
## 版本要求
适用于PC版微信3.9.11.17使用，微信安装包下载：
[点击下载](https://github.com/tom-snow/wechat-windows-versions/releases/download/v3.9.11.17/WeChatSetup-3.9.11.17.exe)
|  环境  | 版本 |
| :----: | :--: |
|   OS   | [![Windows](https://img.shields.io/badge/Windows-10\|11\|Server2016+-white?logo=windows&logoColor=white)](https://www.microsoft.com/)  |
|  微信  | [![Wechat](https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-3.9.11.X-07c160?logo=wechat&logoColor=white)](https://pan.baidu.com/s/1FvSw0Fk54GGvmQq8xSrNjA?pwd=vsmj) |
| Python | [![Python](https://img.shields.io/badge/Python-3.X-blue?logo=python&logoColor=white)](https://www.python.org/) **(不支持3.7.6和3.8.1)**|
## 使用说明
将代码中API部分的KEY等关键信息换成自己的KEY即可使用AI自动回复，其他使用相关内容请参考[wxauto官方使用文档](https://wxauto.loux.cc/docs/intro)
## 修改举例
### 讯飞星火大模型
SPARKAI_URL、SPARKAI_APP_ID、SPARKAI_API_SECRET、SPARKAI_API_KEY、SPARKAI_DOMAIN 需要修改为自己的参数值
```
#星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = ''
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = ''
SPARKAI_API_SECRET = ''
SPARKAI_API_KEY = ''
#星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = ''
```
### 百度千帆大模型
API_KEY、SECRET_KEY 需要修改为自己的参数值
```
API_KEY = "YOUR API_KEY"
SECRET_KEY = "YOUR SECRET_KEY"
```
### Gemini
将url末尾“=”后的内容修改为自己的Gemini APIKEY
```
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=你的APIKEY'
```
### 相关平台
[讯飞星火大模型](https://www.xfyun.cn/doc/spark/Web.html)  
[百度千帆大模型](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/6ltgkzya5)  
[Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn)  
[更多大语言模型API](https://www.meoai.net/free-api.html)  
