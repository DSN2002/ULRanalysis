# 用python来联动mpv与youget指令
有没有觉得用you-get指令来看视频很麻烦，只输入url不好吗？现在就有这样一个懒人包来帮助你完成除了输入url之外的所有事，当然你要输入几个数字。
## 大体介绍  
这个脚本需要mpv和python youget指令的支持，通过调用cmd或powershell来做到自动完成以下操作：  
1，导入视频或歌曲到mpv播放  
2，解析url并显示真实的url连接  
3，加载cookie以在线观看视频  
4，下载非会员或会员(需要cookie)观看的视频  
5，解析url下所有文件的信息  
6，文件的下载地址默认会建立在D盘的video文件下，没有的话会新建一个  
~~6，对于有多个文件的现在还不能读取，可能是编码问题，对模式2 4有影响，待以后修复或蹲一个大佬。~~(已解决)  
对于上传的mpv.conf和input.conf是mpv的配置文件，已经写好了相应的注释，其中input.conf中有Anime4K的快捷键，若是想使用Anime4K请查看Anime4K官方的说明  
  
##更新计划：  
1，添加用户自己选择清晰度下载选项  
2，修复-c模式的问题(并不是破解会员下载限制)
3，待添加...  
  
##已知问题：  
1.下载有非常多集数的视频会报错，应该可以在自行选择清晰度的版本得到解决
2，...
  
## 各个模式的展示:  
### 调用mpv导入视频:  
![模式1](https://github.com/DSN2002/-youget-mpv-python-/blob/main/%E8%A1%A8%E7%A4%BA/mod%201.jpg)  
  
### 解析url:  
  
![模式2](https://github.com/DSN2002/-youget-mpv-python-/blob/main/%E8%A1%A8%E7%A4%BA/mod%202.png)  
  
### 加载cookie看在线视频:  
这一条展示无法使用，等待修复
  
### 下载视频:  
显示多个清晰度的信息  
![模式4](https://github.com/DSN2002/-youget-mpv-python-/blob/main/%E8%A1%A8%E7%A4%BA/mod%204.png)  
  
### 解析url下的文件信息:  
显示多个清晰度的信息  
![模式5](https://github.com/DSN2002/-youget-mpv-python-/blob/main/%E8%A1%A8%E7%A4%BA/mod%205%20%E5%A4%9Ap.png)  
  
## 用到的所有程序的官方连接如下：  
### [Anime4K](https://github.com/bloc97/Anime4K)  
### [you-get](https://github.com/soimort/you-get)  
### [mpv](https://mpv.io/)  
### [you-get与Anime4K的使用方法blibli](https://www.bilibili.com/read/cv12828208)
