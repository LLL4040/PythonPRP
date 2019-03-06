#-*- coding:utf-8 -*-
from data_deal import *
from download import *
from django.shortcuts import render
from django.http import StreamingHttpResponse

def download_model(un):#接受来自view的命令，从数据库中提取数据进行下载
    def file_iterator(file_name, chunk_size=512):#用于形成二进制数据
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name = un + "file.xlsx"#要下载的文件路径
    response = StreamingHttpResponse(file_iterator(the_file_name))#这里创建返回
    response['Content-Type'] = 'application/vnd.ms-excel'#注意格式 
    response['Content-Disposition'] = 'attachment;filename="毕业审核表格.xlsx"'
    return response
