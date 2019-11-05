# pyquery用法
# 类似于jquery，常用CSS选择器

# 1.初始化
# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''

# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))

# URL初始化
# from pyquery import PyQuery as pq
# doc = pq(url='https://cuiqingcai.com')
# print(doc('title'))

# 2.基本的CSS选择器
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
#
# from pyquery import  PyQuery as pq
# doc = pq(html)
# print(doc('#container .list li')) #从外层一层一层往内嵌套
# print(type('#container .list li'))


# 3.查找结点
# 子孙节点
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)

# 子节点
# lis = items.children()
# print(type(lis))
# print(lis)

# 进一步筛选class为active的节点
# lis = items.children('.active')
# print(lis)

# 父节点
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)

# 祖先节点
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# parents = items.parents()
# print(type(parents))
# print(parents) #这里输出两个节点：一个是class为wrap的节点，一个是id为container的节点

# 如果想单独得到一个wrap节点
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# parents = items.parents('.wrap')
# print(type(parents))
# print(parents)

# 兄弟节点
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings()) #这里输出四个兄弟节点

# 进一步筛选某个兄弟节点，可以向siblings方法传入css选择器
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings('.active'))

# 遍历
# 对于单个节点来说
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li)
# print(str(li))

# # 对于多个节点来说
# from pyquery import PyQuery as pq
# doc = pq(html)
# lis = doc('li').items() #采用items得到的是一个生成器，可以进行遍历
# print(type(lis))
# for li in lis:
#     print(li,type(li))

# 4.获取信息
# （1）获取属性
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a,type(a))
# print(a.attr('href'))

# （2）获取文本
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a.text())

# 获取html文本
# li = doc('.item-0.active')
# print(li.html())

# 5.节点的操作(可以改变节点的属性)
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
#
# li.remove_class('active')
# print(li)
#
# li.add_class('active')
# print(li)

# li.css() li.attr()
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active') #"item-0 active"
# print(li)
# li.attr('name', 'link') #"item-0 active" name="link"
# print(li)
# li.css('font-size', '14px') #"item-0 active" name="link" style="font-size: 14px"
# print(li)

# remove方法
#
# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''

# from pyquery import PyQuery as pq
# # # doc = pq(html)
# # # wrap = doc('.wrap')
# # # print(wrap.text())
# # #
# # # wrap.find('p').remove()
# # # print(wrap.text())

# CSS的伪类选择器
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)') #索引是从0开始
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)

# 官方文档
# http://pyquery.readthedocs.io/