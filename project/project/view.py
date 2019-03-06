#-*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from spider import *
from Student import models
import xlsxwriter
from controller import data_deal
from controller import manager
from django.views.decorators.csrf import csrf_exempt

username = ''
def index(request):
    global show_data,username
    username = ''
    show_data = []
    warning = "未登录请先登录"
    return render(request, 'index.html', {'warning':warning, 'username':username, 'alertwords':'JAccount统一身份登录'})

def login(request):
    #登录调用driver
    if request.method != "POST":
        global dri
        dri = driver()
        handles = dri.window_handles
        if len(handles) >= 1:
            for i in range(1,len(handles)):
                dri.switch_to_window(handles[i])
                dri.close()
                dri.switch_to_window(handles[0])
        return render(request, 'login.html', {'warning': ""})
    
    else:
        global username
        form = models.UserLogin(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            icode = form.cleaned_data['icode']
            #异常处理
            try:
                dri.find_element_by_id("user")
            except:
                global dri
                dri = driver()
                handles = dri.window_handles
                if len(handles) >= 1:
                    for i in range(1,len(handles)):
                        dri.switch_to_window(handles[i])
                        dri.close()
                        dri.switch_to_window(handles[0])
                return render(request, 'login.html', {'warning': ""})

            pre_data = get_data(dri, username, password, icode)
            if pre_data == False:
                dri.close()
                global dri
                dri = driver()
                handles = dri.window_handles
                if len(handles) >= 1:
                    for i in range(1,len(handles)):
                        dri.switch_to_window(handles[i])
                        dri.close()
                        dri.switch_to_window(handles[0])
                return render(request, 'login.html', {'warning': "登录失败"})
            
            data = data_deal.data_deal(pre_data,username)
            for i in range(len(data)):
                newi = data[i].__dict__
                data[i] = newi
            code_list = ['SE112','SE418','SE419','SE420','SE422','SE417','SE315','EI901']
            name_list = ["软件工程职业素养， SE112","软件产品设计与用户体验，SE418","企业软件质量保证，SE419","软件知识产权保护，SE420",
                "企业软件过程与管理，SE422","软件工程经济学，SE417","操作系统，SE315","工程实践与科技创新，EI901"]
            base_list = ["序号","学号","姓名","院系","专业","年级","毕业时间","学籍状态","不及格门数","目前修读核心课程学分",
                "暂未修读课程","修读完某一方向","其他方向总学分","人文、社科、自然、计算机、体育、两课、英语"]
            show_list = base_list + name_list
            show_message = ''
            for i in show_list:
                show_message = show_message + '<th>' + i + '</th>'
            
            global show_data
            show_data = [show_message] + [code_list] + [data]
            
            return render(request, 'index.html', {'warning': '', 'username': username, 'alertwords':''})
        return render(request, 'login.html', {'warning': "用户名或密码不正确"})

show_data = []
@csrf_exempt
def extra(request):
    global show_data,username
    if request.method == "POST":
        
        code_list = []
        name_list = []
        base_list = ["序号","学号","姓名","院系","专业","年级","毕业时间","学籍状态","不及格科目","目前修读核心课程学分",
                "暂未修读课程","修读完某一方向","其他方向总学分","人文、社科、自然、计算机、体育、两课、英语"]
        #获取待审核科目
        List = request.POST.keys()[0]
        extraList = json.loads(List)
        print username
        for ex in extraList:
            course_id = ex['id']
            course_name = ex['name']
            code_list += [course_id]
            name_list += [course_name+','+course_id]
        show_list = base_list + name_list
        show_message = ''
        for i in show_list:
            show_message = show_message + '<th>' + i + '</th>'
        data_list = data_deal.get_data_from_file(username,code_list,name_list)
        for i in range(len(data_list)):
            newi = data_list[i].__dict__
            data_list[i] = newi
        show_data = [show_message] + [code_list] + [data_list]
        return HttpResponse("succeed")
    if request.method == "GET":
        
        return HttpResponse(json.dumps(show_data))

def download(request):
    global username
    if username != '':
        return manager.download_model(username)
    return render(request, 'download.html')
    