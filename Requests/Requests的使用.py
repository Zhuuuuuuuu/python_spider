# Requests 详细用法

# 作用：比urllib方便太多

# 1.get请求

# import  requests
# r = requests.get("http://www.baidu.com")
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# 简单的get请求
# import requests
# response = requests.get('http://httpbin.org/get')
# print(response.text)

# 带参数GET请求：附加额外的信息
# import requests
# data = {
#     "name":"genemy",
#     "age":22
# }
# r = requests.get("http://httpbin.org/get",params=data)
# print(r.text)

# 将字符串格式的文字转化为字典 解析json
# import requests
# r = requests.get("http://httpbin.org/get")
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

# 获取二进制数据
# import requests
# # r = requests.get("https://github.com/favicon.ico")
# # print(r.text) #这里会出现乱码 因为是二进制数据转化为字符串
# # print(r.content) #这里打印的是二进制数据

# 创建一个会话来保存图片
# import requests
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico','wb') as f:
#     f.write(r.content)

# 添加headers
# import requests
# r = requests.get("https://www.zhihu.com/explore")
# print(r.text) #不添加就会报错

# 添加了headers 并加上User-Agent信息就不会有问题了(知乎为例)
# import requests
# headers = {
#      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore",headers = headers)
# print(r.text)

# 2.POST请求

# import requests
# data = {
#     "name":"gesgs",
#     "age":22
# }
# r = requests.post("http://httpbin.org/post", data = data)
# print(r.text)

# 添加data和headers的post请求
# import requests#
# data = {'name': 'germey', 'age': '22'}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# response = requests.post("http://httpbin.org/post", data=data, headers=headers)
# print(response.json())

# 3.响应
# import requests
# r = requests.get("http://www.jianshu.com")
# print(type(r.status_code),r.status_code)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)
# print(type(r.url),r.url)
# print(type(r.history),r.history)

# 状态码判断
# import requests
# response = requests.get('http://www.jianshu.com')
# exit() if not response.status_code == 200 else print('Request Successfully')

# import requests
# response = requests.get('http://www.jianshu.com')
# exit() if not response.status_code == requests.codes.not_found else print('404 Not Found')

# 4.高级用法

#上传文件
# import requests
# files = {
#     "file":open("favicon.ico",'rb') #这里传入的是字节流
# }
# r = requests.post("http://httpbin.org/post", files = files)
# print(r.text)

#Cookies
# import  requests
# r = requests.get("http://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items(): #这里用items()方法将RequestCookieJar 转化为元组组成的列表，遍历输出每一个Cookie的名称和值
#     print(key + "=" +value)

#会话的维持

#两次请求相当于打开了两个浏览器，是两个完全不相关的会员，不能成功获取个人信息
# import requests
# requests.get('http://httpbin.org/cookies/set/number/123456789') #这里set方法设置了cookies
# r = requests.get('http://httpbin.org/cookies')#这里通过get方法想得到cookies
# print(r.text) #"cookies": {}

# 解决的方法是建立一个会话
# import  requests
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# SSL证书的验证
# import requests
# response = requests.get('https://www.12306.cn',verify = False)
# print(response.status_code)

# import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)
# #可以指定路径
# import requests
#
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)

# 设置代理
# import requests
# # proxies = {
# #     "http": "http://127.0.0.1:9743",
# #     "https": "https://127.0.0.1:9743",
# # }
# #
# # response = requests.get("https://www.taobao.com",proxies = proxies)
# # print(response.status_code)
# #代理有密码
# import requests
# proxies = {
#     "http": "http://user:password@127.0.0.1:9743/",
# }
# response = requests.get("https://www.taobao.com", proxies=proxies)
# print(response.status_code)
# #使用socks代理
# import requests
#
# proxies = {
#     'http': 'socks5://127.0.0.1:9742',
#     'https': 'socks5://127.0.0.1:9742'
# }
# response = requests.get("https://www.taobao.com", proxies=proxies)
# print(response.status_code)


# 超时设置
# import requests
# # # from requests.exceptions import ReadTimeout
# # # try:
# # #     response = requests.get("http://httpbin.org/get", timeout = 0.001)
# # #     print(response.status_code)
# # # except ReadTimeout:
# # #     print('Timeout')

# 身份验证
# requests自带身份验证功能
# import  requests
# from requests.auth import HTTPBasicAuth
# r = requests.get("",auth = HTTPBasicAuth("username","password"))
# print(r.status_code)

# import requests
# r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
# print(r.status_code)

# 异常处理
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
try:
    response = requests.get("http://httpbin.org/get", timeout = 0.05)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except ConnectionError:
    print('Connection error')
except RequestException:
    print('Error')

try:
    response = requests.get("http://httpbin.org/get", timeout = 0.05)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("Connection error")
except RequestException:
    print("Error")