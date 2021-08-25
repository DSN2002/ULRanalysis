# -*- coding: utf-8 -*-
# 懒人脚本.py
# @作者 肆赧(DSN2002)
# @个人主页 https://github.com/DSN2002
# @创建日期 2021-08-25T09:36:14.084Z+08:00
# @最后修改日期 2021-08-25T16:39:50.993Z+08:00
#

import os
i = 0
while i < 1:
    URL = input(str('input URL \n'))
    print("1导入mpv观看，2显示视频真url，3以-c模式观看登录视频，4下载视频，5查看该url下视频格式")
    num = input("请选择解析方式 \n")
    N   = int(num)
    if N == 1:
        A    = 'you-get -p mpv'
        cmd  = A + ' ' + URL
        info = str(cmd)
        os.system(info)
    elif N == 2:
        A    = 'you-get -u '
        cmd  = A + URL
        info = str(cmd)
        os.system(info)
    elif N == 3:
        cookie = str(input("请输入该视频cookie的路径\n"))
        A      = 'you-get -c=' + cookie + '-p mpv'
        cmd    = A + ' ' + URL
        info   = str(cmd)
        os.system(info)
    elif N == 4:
        print("该模式会自动下载最高画质")
        VIP = int(input("该视频是否需要VIP(1=是，0等于否)\n"))
        if VIP == 0:
            A    = 'you-get -o'
            cmd  = A + ' D:\lenovo\Videos ' + URL  # 若要修改储存位置请替换注意前后都有空格
            info = str(cmd)
            os.system(info)
        else:
            cookie = str(input("请输入该视频cookie的路径\n"))
            A      = 'you-get -c=' + cookie + '-o'
            cmd    = A + ' D:\lenovo\Videos ' + URL  # 若要修改储存位置请替换注意前后都有空格
            info   = str(cmd)
            os.system(info)
    else:
        A    = 'you-get -i '
        cmd  = A + URL
        info = str(cmd)
        os.system(info)
    i = int(input("1退出，0继续\n"))
