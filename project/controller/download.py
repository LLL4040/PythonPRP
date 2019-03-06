#-*- coding:utf-8 -*-
import xlsxwriter
def download(un,data_list,code_list,name_list):#通过数据对本地的Excel文件进行更改
    #创建一个Excel文件
    excelname = un + 'file.xlsx'
    workbook = xlsxwriter.Workbook(excelname)
    #创建一个工作表sheet对象
    worksheet = workbook.add_worksheet()
    #创建数据
    base_list = ["序号","学号","姓名","院系","专业","年级","毕业时间","学籍状态","不及格门数","目前修读核心课程学分",
                "暂未修读课程","修读完某一方向","其他方向总学分","人文、社科、自然、计算机、体育、两课、英语"]
    #name_list = ["软件工程职业素养， SE112","软件产品设计与用户体验，SE418","企业软件质量保证，SE419","软件知识产权保护，SE420",
    #            "企业软件过程与管理，SE422","软件工程经济学，SE417","操作系统，SE315","工程实践与科技创新，EI901"]
    #code_list = ['SE112','SE418','SE419','SE420','SE422','SE417','SE315','EI901']

    list_show = [base_list + name_list]

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
        for course in code_list:
            list_of_one += [i.others[course]] 
        list_show += [list_of_one]
    #print list_show
    #向单元格写入数据
    row = len(data_list) + 1
    column = len(base_list) + len(code_list)  #列数
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