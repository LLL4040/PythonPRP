#-*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from spider import *
from Student import models
import xlsxwriter
from controller import data_deal
from django.views.decorators.csrf import csrf_exempt

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
        handles = dri.window_handles
        if len(handles) >= 1:
            for i in range(1,len(handles)):
                dri.switch_to_window(handles[i])
                dri.close()
                dri.switch_to_window(handles[0])
        return render(request, 'login.html', {'warning': ""})
    
    else:
        form = models.UserLogin(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            icode = form.cleaned_data['icode']
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
            #pre_data = get_soup_data()
            data = data_deal.data_deal(pre_data,username)
            #data = data_deal.get_data_from_file(username)
            return render(request, 'index.html', {'x': 1, 'warning': "点击以上按钮即可显示或下载审核结果", 'data': data})
        return render(request, 'login.html', {'warning': "用户名或密码不正确"})


@csrf_exempt
def extra(request):
    global a
    if request.method == "POST":
        code_list = []
        name_list = []
        base_list = ["序号","学号","姓名","院系","专业","年级","毕业时间","学籍状态","不及格门数","目前修读核心课程学分",
                "暂未修读课程","修读完某一方向","其他方向总学分","人文、社科、自然、计算机、体育、两课、英语"]
        username = 'zhuangying'
        List = request.POST.keys()[0].split(',[',1)
        extraList = json.loads(List[0])
        name = json.loads(List[1].split(']')[0])
        n = name['username']
        print n
        #username = n
        for ex in extraList:
            course_id = ex['id']
            course_name = ex['name']
            print course_id
            print course_name
            code_list += [course_id]
            name_list += [course_name+','+course_id]
        show_list = base_list + name_list
        show_message = ''
        for i in show_list:
            show_message = show_message + '<th>' + i + '</th>'
        print show_message
        data_list = data_deal.get_data_from_file(username,code_list,name_list)
        print data_list[0].others
        show_data = [show_message] + [code_list] + [data_list]
            

        a = [{"a":"aa","b":"bb"},{"a":"cc","b":"dd"}]
        return HttpResponse("succeed")
    if request.method == "GET":
        print a
        return HttpResponse(json.dumps(a))



    