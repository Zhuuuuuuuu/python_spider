import urllib.request
import urllib.parse
import socket
import urllib.error
from urllib import request,parse

# 1.urlopen
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))
# print(type(response))

# print(response.status)
# print(response.getheaders())
# print(response.getheaders("Server"))

# data参数：这里设置了urlopen的第二个参数，传入了参数
# data = bytes(urllib.parse.urlencode({"word":"hello"}),encoding="utf8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read())

#timeout参数 :用于设置超时时间，请求超出了设置的这个时间，还没得到响应，就会抛出异常
# response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
# print(response.read())

# 这里可以设置一个超时时间来控制一个网页在长时间未响应时，就跳过他的抓取
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print("timeout")


# 2.Request:urlopen()方法可以实现最基本请求的发起，但这几个简单的参数并不足以构建整个完整的请求，请求中需要添加headers信息
# 将urlopen()改变为一个request对象
# requset = urllib.request.Request("http://httpbin.org")
# response = urllib.request.urlopen(requset)
# print(response.read().decode("utf-8"))

# request传入多个参数
# url = "http://httpbin.org"
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data =bytes(parse.urlencode(dict),encoding="utf-8")
# req = request.Request(url=url,data=data,headers=headers,method="post")
# response = request.urlopen(req)
# print(response.read().decode("utf-8"))

# 方式二
# from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# Handler：设置代理
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())

# Cookies:用于维持会话,下面代码用来如何获取网站的cookies
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print(item.name + "=" +item.value)

# cookies实际上也是以文本形式保存的
# 这里是以Mozilla子类进行保存数据
# import http.cookiejar, urllib.request
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# cookies也可以使用LWP格式进行读取和保存
# import http.cookiejar, urllib.request
# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# 读取lwp格式的cookie
# import http.cookiejar, urllib.request
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie-lwp.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# 3.处理异常
# 一：URLError:来自于urllib库的error模块
# from urllib import request,error
# try:
#     response = request.urlopen('http://www.sdnfkadsas.com')
# except error.URLError as e:
#     print(e.reason)

# 二：HTTPError：是URLError的子类，专门用来处理HTTP请求错误
# code:返回HTTP状态码，404表示不存在
# reason:同父类一样，用于返回错误的原因
# headers：返回请求头

# from urllib import request, error
#
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# 有时候,reason属性返回的不一定是字符串，也有可能是一个对象
# import socket
# # import urllib.request
# # import urllib.error
# #
# # try:
# #     response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
# # except urllib.error.URLError as e:
# #     print(type(e.reason))
# #     if isinstance(e.reason, socket.timeout):
# #         print('TIME OUT')


# URL解析
# 1.urlparse():该方法可以实现URL的识别和分段
# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)

# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
#以上urlparse()函数解析将其拆分成6个部分，
# 有scheme = http ,netloc = www.baidu.com,
# path = /index.html,params = users
# query = "id=5",fragment="comment")
# scheme代表协议，netloc代表域名，path代表访问路径，params代表参数，query=查询条件，
# 后面是锚点，用于直接定位页面内部的下拉位置
# 一个链接的标准格式就是：scheme://netloc/path;params?query#fragment

# 2.urlunparse()：他接收的参数是一个可迭代的对象，但是它的长度必须是6,这样可以成功实现url的构造
# from urllib.parse import urlunparse
# data = ['http','www.baidu.com','index.html','user','a=6','comment']
# print(urlunparse(data))

# 3.urljoin()
# from urllib.parse import urljoin
#
# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))

# 4.urlencode()
from urllib.parse import urlencode
params = {
    'name':'genme',
    'age':22
}
base_url = 'http://www.baidu.com'
url = base_url + urlencode(params)
print(url)