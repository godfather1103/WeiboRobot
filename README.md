# WeiboRobot
#### 微博机器人，用于自动发微博和回复评论
本程序需要在config目录下创建一个myConfig.py文件<br/>
文件内容格式可以参照myConfig-init.py<br/>
填完信息后windows下双击startup.bat就可以启动，<br/>
如果安装了Python，执行python robot.py也可以启动<br/>
在res文件夹下设置发布的微博内容（greet.txt），回复评论的内容（comment.txt）和图片（image文件夹下）<br/>
[演示地址](http://weibo.com/godfather1103)(不一定常开)

## 引用的第三方模块（本程序中已包含）
1、[微博的Python SDK](http://github.liaoxuefeng.com/sinaweibopy/)<br/>
2、python的RSA模块


### 最后说几句
本程序在Linux下与windows下运行部分情况会有些许不同，主体功能都是相同的！<br/>
目前这个程序回复评论的内容和自动发送的微博内容需要手动设置，在后续中可能会增加智能回复功能<br/>
本程序并非原创，是在[QRobot](https://github.com/GinSmile/QRobot)的基础上修改而成<br/>
## 最近说明
由于新浪微博相关接口调整，这个程序目前未升级接口，相关操作暂时不确保是否能用。



