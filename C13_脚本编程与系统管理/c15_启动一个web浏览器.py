# 问题:通过脚本启动浏览器并打开指定的url网页
# 用 webbrowser 模块
import webbrowser

c = webbrowser # .get('firefox') 不好用
c.open('www.baidu.com')
c.open_new_tab('www.baidu.com')