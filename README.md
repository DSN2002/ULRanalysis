# 用python来联动mpv与youget指令
有没有觉得用you-get指令来看视频很麻烦，只输入url不好吗？现在就有这样一个懒人包来帮助你完成除了输入url之外的所有事，当然你要输入几个数字。

这个脚本需要mpv和python youget指令的支持，通过调用cmd或powershell来做到自动完成以下操作：  
1，导入视频或歌曲到mpv播放  
2，解析url并显示真实的url连接  
3，加载cookie以在线观看视频  
4，下载非会员或会员(需要cookie)观看的视频  
5，解析url下所有文件的信息  
对于上传的mpv.conf和input.conf是mpv的配置文件，已经写好了相应的注释，其中input.conf中有Anime4K的快捷键，若是想使用Anime4K请查看Anime4K官方的说明
