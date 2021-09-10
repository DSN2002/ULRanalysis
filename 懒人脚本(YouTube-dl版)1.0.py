# -*- coding: utf-8 -*-
# @Author: 肆赧(DSN2002)
# @Date:   2021-08-23 18:15
# @Last Modified by:   肆赧(DSN2002)
# @Last Modified time: 2021-09-10 15:12

import os
i = 0
while i < 1:
    URL = input(str('input URL \n'))
    print("1导入mpv观看，2显示视频真url，3下载视频，4查看该url下视频格式")
    num = input("请选择解析方式 \n")
    N   = int(num)
    if N == 1:
        cmd  = 'mpv ' + URL
        info = str(cmd)
        os.system(info)
    elif N == 2:
        cmd  = 'you-get -u ' + URL
        info = str(cmd)
        os.system(info)
    elif N == 3:
        mod = int(input("是否下载所有剧集(1=是，0=单集)\n"))
        if mod == 0:
            print("该模式会自动下载最高画质")
            VIP = int(input("该视频是否需要VIP(1=是，0等于否)\n"))
            if VIP == 0:
                cmd  = 'you-get -o' + ' D:\Videos ' + URL  # 若要修改储存位置请替换注意前后都有空格
                info = str(cmd)
                print("自动下载开启中，去活动一下吧！")
                os.system(info)
            else:
                cookie = str(input("请输入该视频cookie的路径\n"))
                cmd    = 'you-get -c ' + cookie + ' -o' + ' D:\Videos ' + URL  # 若要修改储存位置请替换注意前后都有空格
                print("自动下载开启中，去活动一下吧！")
                info   = str(cmd)
                os.system(info)
        else:
            print("该模式会自动下载最高画质")
            VIP = int(input("该视频是否需要VIP(1=是，0等于否)\n"))
            fold = str(input("请以 \名字 为格式存放视频的文件夹命名\n"))
            if VIP == 0:
                cmd  = 'you-get -o' + ' D:\Videos' + fold + ' ' + '--playlist '+ URL  # 若要修改储存位置请替换注意前后都有空格
                info = str(cmd)
                print("自动下载开启中，去活动一下吧！")
                os.system(info)
            else:
                cookie = str(input("请输入该视频cookie的路径\n"))
                cmd    = 'you-get -c ' + cookie + ' -o' + ' D:\Videos' + fold + ' ' + '--playlist ' + URL  # 若要修改储存位置请替换注意前后都有空格
                info   = str(cmd)
                print("自动下载开启中，去活动一下吧！")
                os.system(info)
    else:
        cmd  = 'you-get -i ' + URL
        info = str(cmd)
        os.system(info)
    i = int(input("1退出，0继续\n"))
