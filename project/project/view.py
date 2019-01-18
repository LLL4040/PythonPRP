#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from spider import *
from Student import models
import xlsxwriter
from controller import data_deal

def index(request):
    x = 1#再修读其他方向门数
    warning = "未登录请先登录"
    data = []
    if request.method == "POST":
        form = models.CrossNumber(request.POST)
        if form.is_valid():
            num = form.cleaned_data['num']
            if num >= 0:
                x = num
    return render(request, 'index.html', {'x':x, 'warning':warning, 'data':data})

def login(request):
    if request.method != "POST":
        global dri
        dri = driver()
        return render(request, 'login.html', {'warning': ""})
    
    else:
        form = models.UserLogin(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            icode = form.cleaned_data['icode']
            pre_data = get_data(dri, username, password, icode)
            #pre_data = get_soup_data()
            data = data_deal.data_deal(pre_data)
            return render(request, 'index.html', {'x': 1, 'warning': "点击以上按钮即可显示或下载审核结果", 'data': data})
        return render(request, 'login.html', {'warning': "用户名或密码不正确"})

    