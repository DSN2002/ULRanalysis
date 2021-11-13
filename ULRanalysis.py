# -*- coding: utf-8 -*-
#* Author: DSN2002
#* Date: 2021-11-12 17:40
#* LastEditTime: 2021-11-13 18:42
#* LastEditors: DSN2002
#* Description:
#* 仅供研究使用，请勿用于其他活动
#

import easygui as g                                 #* 调用gui库
import time                                         #* 调用时间库
from ctypes import *                                #* 调用运行库
import os                                           #* 调用系统库

#* 检查当前程序版本
with open(r'./version/setting.txt','a+',encoding='utf-8') as test:     #* 获取设置文件的相对路径
    localversion = test.readline()                                      #* 获取本地程序版本
    path = test.readline()                                              #* 获取存放下载文件的位置
    cookie = test.readline()                                            #* 取得cookie文件的位置

#* 取得当前的相对路径，取得dll位置
result = 0
dllpath = os.getcwd()                   #*取得当前路径
uppath = dllpath + "\\version"
dllpath = dllpath + "\\dll"
os.add_dll_directory(str(dllpath))
updll = cdll.LoadLibrary(str(dllpath) + "\\updata.dll")
result = cdll.LoadLibrary(str(dllpath) + "\\lazycode.dll")

## 主程序块

n = 1
q = 1
while n > 0:
    while q > 0:
        ulr = g.enterbox(msg="请输入ulr", title="懒人脚本" + str(localversion),strip=True)
        if ulr[0:4] != "http":  ## 判断ulr是否为空
            g.msgbox(msg="请输入正确的ulr", title="错误", ok_button="OK", image=None, root=None)
        if ulr[0:4] == "http":
            break
    num = ["用mpv观看","显示视频真ulr","下载视频","查看该ulr下视频信息","设置"]
    mode = g.buttonbox(msg="请选择解析方式（没事不要乱进设置，不然要重新选择cookie和存放路径）", title="懒人脚本", choices=num)
    start_time = time.time()            #* 开始计算处理时间

    #* 对bilbil的ulr进行处理，加快解析速度
    bilulr =ulr[8:24]
    print(bilulr)
    i = 0
    if str(bilulr) == "www.bilibili.com":
        while i < 100:
            if ulr[i] != '?':
                i = i + 1
            else:
                break
        ulr = ulr[0:i]
    ulr = ulr.encode('ascii')            #* 将ulr转为C.dll能识别的ASCII码

## 用mpv观看 模式一

    if mode == "用mpv观看":
        choices = ["youtube-dl","youget"]
        msg_txt = "选择解析模式，bilbil用youtube-dl，腾讯视频用youget,其他随意"
        n = g.buttonbox(msg=msg_txt, title="用mpv观看", choices=choices)
        if n == "youtube-dl":
            print(result.ytb_w(ulr))            #* 调用C.dll内youtube-dl的算法，顺便显示出ulr方便识别错误
            end_time = time.time()              #* 得出处理时间
            print("总共用时%s"%(end_time-start_time))
        else:
            print(result.ygt_w(ulr))            #* 调用C.dll内you-get的算法，顺便显示出ulr方便识别错误
            end_time = time.time()              #* 得出处理时间
            print("总共用时%s"%(end_time-start_time))

## 显示视频真ulr 模式二

    elif mode == "显示视频真ulr":
            print(result.y_u(ulr))              #* 调用C.dll内you-get 解析存视频在服务器中地址
            end_time = time.time()              #* 得出处理时间
            print("总共用时%s"%(end_time-start_time))

## 下载视频 模式三

    elif mode == "下载视频":
        choices = ["单集下载","全集下载"]
        msg_txt = "请选择下载方式"
        n = g.buttonbox(msg=msg_txt, title="下载视频", choices=choices)
        #* 单集下载
        if n == "单集下载":
            choices = ["是","否"]
            msg_txt = "该模式会自动下载最高画质,该视频是否需要VIP?"
            VIP = g.buttonbox(msg=msg_txt, title="下载视频", choices=choices)
            #* 调用C.dll内you-get下载视频
            if VIP == "否":
                print("自动下载开启中，去活动一下吧！")
                print(result.y_od(ulr,path))
                end_time = time.time()              #* 得出处理时间
                print("总共用时%s"%(end_time-start_time))
            else:
                print("自动下载开启中，去活动一下吧！")
                print(result.y_odc(ulr,path,cookie))
                end_time = time.time()              #* 得出处理时间
                print("总共用时%s"%(end_time-start_time))
        #* 全集下载
        else:
            choices = ["是","否"]
            msg_txt = "该模式会自动下载最高画质,该视频是否需要VIP?"
            VIP = g.buttonbox(msg=msg_txt, title="下载全集视频", choices=choices)
            fold = g.enterbox("请为存放视频的文件夹命名","文件夹命名")
            if VIP == "否":
                print("自动下载开启中，去活动一下吧！")
                print(result.y_ad(ulr,path,fold))
                end_time = time.time()              #* 得出处理时间
                print("总共用时%s"%(end_time-start_time))
            else:
                print("自动下载开启中，去活动一下吧！")
                print(result.y_adc(ulr,path,fold,cookie))
                end_time = time.time()              #* 得出处理时间
                print("总共用时%s"%(end_time-start_time))

##查看该ulr下视频信息

    elif mode == "查看该ulr下视频信息":
        print(result.y_l(ulr))
        end_time = time.time()              #* 得出处理时间
        print("总共用时%s"%(end_time-start_time))

## 设置项
    elif mode == "设置":
        loop = 1
        while loop > 0:
            list1 = ['存放位置','cookie的路径','检查更新','退出设置']
            msg_txt = "请选择设置项"
            n = g.buttonbox(msg=msg_txt, title="设置", choices=list1)
            if n == "存放位置":
                path = g.diropenbox()
            if n == "cookie的路径":
                cookie = g.fileopenbox()
            if n == "检查更新":
                with open(r'./version/version.txt','a+',encoding='utf-8') as test:
                    onlinevresion = test.readline()                 #* 获取网络版本的版本
                    upcheckulr = test.readline()                    #* 获取网络版本的更新检查文件的ulr
                    upulr = test.readline()                         #* 获取网络版本的ulr
                print(updll.upcheck(upcheckulr,uppath))
                if str(localversion) != str(onlinevresion):
                    choices = ["下载更新","下次一定"]
                    msg_txt = "有新版本可以下载了!要不要更新呢？"
                    n = g.buttonbox(msg=msg_txt, title="更新程序", choices=choices)
                    if n == "快给我下！":
                        print(updll.updata(upulr,uppath))          #* 下载更新
                else:
                    g.msgbox("当前已经是最新版本了！\n")
            if n == "退出设置":
                with open(r'./version/setting.txt','a+',encoding='utf-8') as test:
                    test.truncate(5)
                    test.write("\n" + str(path) + "\n")
                    test.write(str(cookie) + "\n")
                break
    else:
        break
##  继续运行程序
    n = int(g.ccbox(msg="要继续吗?", title="懒人脚本", choices=("继续", "不了"), image=None))
