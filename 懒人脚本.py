#!/usr/bin/python 
# coding: utf-8

i = 0
while i < 1:
    URL = input(str('input URL \n'))
    GUI = URL
    print ("1导入mpv观看，2显示视频真url，3以-c模式观看登录视频，4下载视频，5查看该url下视频格式")
    num = input("请选择解析方式 \n")
    N = int(num)
    if N == 1:
        A = 'you-get -p mpv'
        import os
        cmd = A + ' ' + GUI
        info = str(cmd)
        os.system(info)
    elif N == 2:
        A = 'you-get -u'
        import os
        cmd = A + ' ' + GUI
        info = str(cmd)
        res = os.popen(info)
        txt = res.read().decode(encoding="utf-8", errors="ignore")
        print(txt)
    elif N == 3:
        cookie = str(input("请输入该视频cookie的路径\n"))
        A = 'you-get -c=' + cookie +  '-p mpv'
        import os
        cmd = A + ' ' + GUI
        info = str(cmd)
        os.system(info)
    elif N == 4:
        print("该模式会自动下载最高画质")
        VIP = int(input("该视频是否需要VIP(1=是，0等于否)\n"))
        if VIP == 0:
            A = 'you-get -o'
            import os
            cmd = A + ' D:\Lenovo\Videos ' + GUI                    #若要修改储存位置请替换D:\Lenovo\Videos，注意前后都有空格
            info = str(cmd)
            os.system(info)
        else:
            cookie = str(input("请输入该视频cookie的路径\n"))
            A = 'you-get -c=' + cookie +  '-o'
            import os
            cmd = A + ' D:\Lenovo\Videos ' + GUI                    #若要修改储存位置请替换D:\Lenovo\Videos，注意前后都有空格
            info = str(cmd)
            os.system(info)
    else:
        A = 'you-get -i'
        import os
        cmd = A + ' ' + GUI
        info = str(cmd)
        res = os.popen(info)
        txt = res.read().decode(encoding="utf-8", errors="ignore")
        print(txt)
    i = int(input("1退出，0继续\n"))
