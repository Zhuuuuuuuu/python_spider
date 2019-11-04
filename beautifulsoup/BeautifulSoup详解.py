# Beautiful Soup
# 使用正则表达式一旦有问题，得到的就不是想要的结果
# 借助网页的节点id或者class来做区分
# 有了beautiful Soup就不用再去写一些复杂的正则表达式

# 1.基本使用
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,"lxml")
# print(soup.prettify())
# print(soup.title.string)

# 2.选择元素
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)

# 3.提取信息
# （1）获取名称
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

# print(soup.title.name)

# (2)获取属性
# print(soup.p.attrs)
# print(soup.p.attrs['name'])

# 或者
# print(soup.p['name'])
# print(soup.p['class'])

# (3)获取内容
# print(soup.p.string)

# 4.嵌套选择
# print(soup.head.title.string)

# 5.关联选择
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
# （1）子节点和子孙节点
# 直接调用【子节点】,可以使用contents属性,返回的是列表的形式
# print(soup.p.contents)

# 【子节点】还可以调用children方法来得到相应的结果
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'lxml')
# # print(soup.p.children) #这里得到的是一个迭代器，返回的是地址值 <list_iterator object at 0x000001A59ACBF550>
# for i,child in enumerate(soup.p.children):
#     print(i,child)

# 【子孙节点】还可以调用descendants属性
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'lxml')
# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)

# （2）父节点和祖先节点
# 【父节点】使用parent属性
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'lxml')
# print(soup.a.parent)

# 【祖先节点】可以调用parents属性
# print(soup.a.parents) #返回的结果还是一个迭代器，<generator object parents at 0x000001C9BA0B4A98>
# print(type(soup.a.parents))
# print(list(soup.a.parents))

# (3)兄弟节点
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'lxml')
# print('Next Sibling',soup.a.next_sibling)
# print('Prenv Sibling',soup.a.previous_sibling)
# print('Next Siblings',list(enumerate(soup.a.next_sibling)))
# print('Prev Sibilngs',list(enumerate(soup.a.previous_sibling)))

# 6.方法选择器
# （1）find_all()方法
# 顾名思义，就是查询所有符合条件的元素
# 给他传入一些属性或者文本，就可以得到符合条件的元素

# 查询name
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name = 'ul')[0]))
# 这里传入的参数值是ul，也就是说，我们想要得到的是所有Ul节点，返回的是一个长度为2的列表
# 可以进行循环打印

# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))


# 查询属性attrs(传入的参数是字典的类型)
# print(soup.find_all(attrs={'id':'list1'}))
# print(soup.find_all(attrs={'name':'elements'}))

# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_ = 'element'))

#查询文本内容text
# 传入的形式可以是字符串，也可以是正则表达式对象
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text='Foo'))

# find_parents() find_parent()¶
# find_parents()返回所有祖先节点，find_parent()返回直接父节点。
#
# find_next_siblings() find_next_sibling()
# find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
#
# find_previous_siblings() find_previous_sibling()
# find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
#
# find_all_next() find_next()
# find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
#
# find_all_previous() 和 find_previous()
# find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点

# (2)find方法
# 返回匹配结果的第一个元素
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.find('ul')) #返回列表里面的第一个值
# print(type(soup.find('ul'))) #返回bs4.elment.tag
# print(soup.find(class_='list')) #返回列表里面的第一个值


# 7.CSS选择器
# 适用于WEB开发
# (1)只需要调用select()方法
# print(soup.select('.panel .panel-heading')) #返回hello的结果
# print(soup.select('ul li')) #返回ul下的li结果
# print(soup.select('#list-2 .element')) #返回list-2下的结果

# (2)嵌套选择
soup = BeautifulSoup(html,'lxml')
# for ul in soup.select('ul'):
#     print(ul.select('li'))

# 这里循环正常输出了所有ul节点下的li组成的列表

# （3）获取属性
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])

# list-1
# list-1
# list-2
# list-2

# (4)获取文本
# for li in soup.select('li'):
#     print('Get Text',li.get_text())
#     print('String',li.String)

# 以上对比可以看出，string方法和get_text()方法得到的结果一致