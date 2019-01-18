#-*- coding:utf-8 -*-
import xlsxwriter
def download(data_list):#通过数据对本地的Excel文件进行更改
    #创建一个Excel文件
    workbook = xlsxwriter.Workbook('file.xlsx')
    #创建一个工作表sheet对象
    worksheet = workbook.add_worksheet()
    #创建数据
    list_show = [["序号","学号","姓名","院系","专业","年级","毕业时间","学籍状态","不及格门数","目前修读核心课程学分",
                "暂未修读课程","修读完某一方向","再修读其他方向一门","人文、社科、自然、计算机、体育、两课、英语",
                "软件工程职业素养， SE112","软件产品设计与用户体验，SE418","企业软件质量保证，SE419","软件知识产权保护，SE420",
                "企业软件过程与管理，SE422","计算机系统基础（1）（上），SE114","程序设计课程设计，SE113","程序设计与数据结构，SE232"]]

    num = 0
    for i in data_list:
        num += 1
        list_of_one = [num]
        list_of_one += [i.student_ID]
        list_of_one += [i.name]
        list_of_one += [i.department]
        list_of_one += [i.major]
        list_of_one += [i.grade]
        list_of_one += [i.graduate_time]
        list_of_one += [i.student_status]
        list_of_one += [i.failed_number]
        list_of_one += [i.center_credits]
        list_of_one += [i.courses_must_to_take]
        list_of_one += [i.one_direction]
        list_of_one += [i.another_direction]
        list_of_one += [i.general_courses]
        list_of_one += [i.others['SE112']]
        list_of_one += [i.others['SE418']]
        list_of_one += [i.others['SE419']]
        list_of_one += [i.others['SE420']]
        list_of_one += [i.others['SE422']]
        list_of_one += [i.others['SE114']]
        list_of_one += [i.others['SE113']]
        list_of_one += [i.others['SE232']]
        list_show += [list_of_one]
    #print list_show
    #向单元格写入数据
    row = len(data_list) + 1
    column = 22  #列数
    for i in xrange(row):
        for j in xrange(column):
            word_list = ['A','B','C','D','E','F','G',
                        'H','I','J','K','L','M','N',
                        'O','P','Q','R','S','T',
                        'U','V','W','X','Y','Z']
            x = word_list[j]
            y = str(i+1)
            data = str(list_show[i][j])
            worksheet.write(x+y,'%s'%(data))
    #关闭并保存文件
    workbook.close()
    return