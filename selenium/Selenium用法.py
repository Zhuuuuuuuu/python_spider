# Selenium的用法
# 对于一些动态网页来说，类似于JavaScript动态渲染的页面来说
# 此种爬取方式非常有效

# 1.基本使用
# 这里需要下载goole的chrome webdriver，并且需要配置环境变量
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# 2.申明浏览器对象
# from selenium import webdriver
# brower = webdriver.chrome
# brower = webdriver.Firefox

# 3.访问页面
# brower = webdriver.Chrome()
# brower.get('https://www.taobao.com')
# print(brower.page_source) #这里打印源代码,并且只有所有图片都加载完成才会打印源代码
# brower.close()

# 4.查找元素
# 单个节点
from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first,input_second,input_third)
# browser.close()
# 这三个节点是同一个节点
# 分别使用ID，CSS选择器，Xpath方式获取

# 多个节点
# 使用find_elements的方法
# browser = webdriver.Chrome()
# # browser.get("https://www.taobao.com")
# # lis = browser.find_elements_by_css_selector('.service-bd li')
# # print(lis)
# # browser.close()
# 这里得到的内容变成了列表的类型，列表中的每个节点都是WebElement类型

# 5.节点的交互
# 输入文字用send_keys()的方法，清空文字用clear()的方法，点击按钮用click()的方法
# import time
# broswer = webdriver.Chrome()
# broswer.get('https://www.taobao.com')
# input = broswer.find_element_by_id('q')
# input.send_keys('iPhone11')
# time.sleep(1)
# input.clear()
# input.send_keys('AJ1')
# button = broswer.find_element_by_class_name('btn-search')
# button.click()


# 6.交互动作
# 这里实现一个拖拽的动作
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 7.执行javaScript
# from selenium import webdriver
# broswer = webdriver.Chrome()
# broswer.get('https://www.zhihu.com/explore')
# broswer.execute_script('window.scrollTo(0,document.body.scrollHeight)') #此处将进度条下拉到最底部
# broswer.execute_script('alert("To Bottom")') #此处弹出已到最底部

# 8. 获取节点的属性
# 获取属性
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

# 获取文本值
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

#获取id,位置，标签名和大小
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.size)
# print(input.tag_name)

# 9.切换frame
# Selenium打开页面后，它默认是在父级Frame中进行操作，而此时如果页面中还有子Frame，它是不能获取到子Frame中的节点的
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No logo') #这里因为切换到了子frame，所有打印no logo
#
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# 10.延时等待
# 隐式等待:找到了就直接输出，没找到就等待一定时间后，如果再没找到，抛出异常
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('CornerButtons')
# print(input)

# 显示等待：指定要查找的节点，设置一个最长等待时间
# 如果在这个时间中加载出来了这个节点,就返回查找的节点
# 如果到了规定时间依然没有加载出该节点,就会抛出异常

# broswer = webdriver.Chrome()
# broswer.get('https://www.taobao.com/')
# wait = WebDriverWait(broswer,10) #这里设置最大等待时间10秒钟
# input = wait.until(EC.presence_of_element_located((By.ID,'q'))) #这里输入的是搜索框'q'
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'btn-search'))) #这里按钮超过10秒没有加载出来
# print(input,button)

# title_is 标题是某内容
# title_contains 标题包含某内容
# presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')
# visibility_of_element_located 元素可见，传入定位元组
# visibility_of 可见，传入元素对象
# presence_of_all_elements_located 所有元素加载出
# text_to_be_present_in_element 某个元素文本包含某文字
# text_to_be_present_in_element_value 某个元素值包含某文字
# frame_to_be_available_and_switch_to_it frame加载并切换
# invisibility_of_element_located 元素不可见
# element_to_be_clickable 元素可点击
# staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
# element_to_be_selected 元素可选择，传元素对象
# element_located_to_be_selected 元素可选择，传入定位元组
# element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
# element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False
# alert_is_present 是否出现Alert
# 详细内容：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# 11.网页的前进和后退
# import time
# from selenium import webdriver
# broswer = webdriver.Chrome()
# broswer.get('https://www.taobao.com/')
# broswer.get('https://www.baidu.com/')
# broswer.get('https://www.python.org/')
# broswer.back()
# time.sleep(1)
# broswer.forward()
# broswer.close()

# 12.Cookies
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'}) #这里传入的是一个字典
# print(browser.get_cookies())
# browser.delete_all_cookies() #这里删除了所有的cookies 所以结果是[]
# print(browser.get_cookies())


# 13.选项卡管理
# 简而言之；就是打开同一个浏览器的新网页
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://python.org')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')

# 14.异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()