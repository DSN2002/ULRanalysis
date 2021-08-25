# 用python来联动mpv与youget指令
有没有觉得用you-get指令来看视频很麻烦，只输入url不好吗？现在就有这样一个懒人包来帮助你完成除了输入url之外的所有事，当然你要输入几个数字。
## 大体介绍  
这个脚本需要mpv和python youget指令的支持，通过调用cmd或powershell来做到自动完成以下操作：  
对于上传的mpv.conf和input.conf是mpv的配置文件，已经写好了相应的注释，其中input.conf中有Anime4K的快捷键，若是想使用Anime4K请查看Anime4K官方的说明  
  
## 更新日志： 
2021.08.26  2.0版更新  
保留了1.0版本的大部分功能  
修复了：  
1，解析url时的报错  
2，解析文件信息时的报错  
添加了：  
1，将文件下载在D盘的video文件夹中，并且下载剧集时可以选择建立文件夹保存剧集  
2，对下载多文件的支持  
删除了：  
1，加载cookies观看在线视频的功能  
2，去除了一些重复的垃圾代码，精简了脚本  
2021.08.24  1.0版发布  
1.0版可以：  
1，导入视频或歌曲到mpv播放  
2，解析url并显示真实的url连接  
~~3，加载cookie以在线观看视频~~  
~~4，下载非会员或会员(需要cookie)观看的视频~~  
5，解析url下所有文件的信息  
  
##已知问题：  
1.下载有非常多集数的视频会报错，在未来某个版本可能解决  
2，以-c加载的cookies下载剧集可能会出现错误(网络问题？？？)
3，待发现...  

## 用到的所有程序的官方连接如下：  
### [Anime4K](https://github.com/bloc97/Anime4K)  
### [you-get](https://github.com/soimort/you-get)  
### [mpv](https://mpv.io/)  
### [you-get与Anime4K的使用方法blibli](https://www.bilibili.com/read/cv12828208)

  
## 各个模式的展示:  
### 调用mpv导入视频:  
![模式1](https://github.com/DSN2002/youget-mpv-python/blob/main/Demo%20pictures/%E6%A8%A1%E5%BC%8F1.png)  
  
### 解析url:  
  
![模式2](https://github.com/DSN2002/youget-mpv-python/blob/main/Demo%20pictures/%E6%A8%A1%E5%BC%8F2.png)  
  
### 下载视频:  
下载视频  
![单个视频](https://github.com/DSN2002/youget-mpv-python/blob/main/Demo%20pictures/%E5%8D%95%E8%A7%86%E9%A2%91%E4%B8%8B%E8%BD%BD.png)  
![多个视频](https://github.com/DSN2002/youget-mpv-python/blob/main/Demo%20pictures/%E5%A4%9A%E8%A7%86%E9%A2%91%E4%B8%8B%E8%BD%BD%E6%A8%A1%E5%BC%8F%20%E4%B8%8B%E8%BD%BD%E5%88%86p%E8%A7%86%E9%A2%91.png)  
![整季动漫](https://github.com/DSN2002/youget-mpv-python/blob/main/Demo%20pictures/%E5%A4%9A%E8%A7%86%E9%A2%91%E4%B8%8B%E8%BD%BD%E6%A8%A1%E5%BC%8F%20%E4%B8%8B%E8%BD%BD%E6%95%B4%E5%AD%A3%E5%8A%A8%E6%BC%AB.png)  
![结果](https://github.com/DSN2002/youget-mpv-python/blob/main/Demo%20pictures/%E8%A7%86%E9%A2%91%E4%B8%8B%E8%BD%BD%E7%BB%93%E6%9E%9C.png)  
  
### 解析文件信息:  
显示多个清晰度的信息  
![模式5](https://github.com/DSN2002/youget-mpv-python/blob/main/Demo%20pictures/%E6%A8%A1%E5%BC%8F4.png)  
