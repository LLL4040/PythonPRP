#-*- coding:utf-8 -*-
from spider import *
from Student import get_and_post
from download import *


def change(one,code_list):
    tmp = {}
    for i in range(len(code_list)):
        tmp[code_list[i]] = '未选课'
    tmplist1 = code_list
    tmplist2 = one.others.split(';')
    for i in tmplist2:
        i = i.split(',')
        for j in tmplist1:
            if j in i[0]:
                if 'P' in i[2]:
                    tmp[j] = u'通过'
                    break
                if 'F' in i[2]:
                    tmp[j] = u'未通过'
                    break
                if '△' in i[2]:
                    if tmp[j] == u'通过':
                        break
                    tmp[j] = u'未通过'
                    break
                if int(float(i[2])) >= 60:
                    tmp[j] = u'通过'
                else:
                    tmp[j] = u'未通过'
    one.others = tmp

def data_deal(list1,username):#list1是从spider.py接受到的原始数据
    list2 = []
    code_list = ['SE112','SE418','SE419','SE420','SE422','SE417','SE315','EI901']

    if list1 != []:
        for person in list1:
            student = data2(person.student_ID, person.name, person.department, person.major, person.grade,
                            person.graduate_time, person.student_status, person.failed_number, person.center_credits,
                            person.courses_must_to_take, person.a_group, person.b_group, person.c_group, person.d_group,
                            person.professional_elective_courses, person.enterprise_education_courses,
                            person.general_courses, person.others, '无', '无')
            #student.change()
            change(student, code_list)

            #处理one_direction, another_direction两项
            a = student.a_group.replace("\xc2\xa0", " ").split(',')
            b = student.b_group.replace("\xc2\xa0", " ").split(',')
            c = student.c_group.replace("\xc2\xa0", " ").split(',')
            d = student.d_group.replace("\xc2\xa0", " ").split(',')
            tmp = [a,b,c,d]
            for group in tmp:
                if len(group) > 2: 
                    if group[2] == ' ':
                        group[2] = 0
            if int(a[2]) + int(a[3]) >= 15:
                student.one_direction = a[0]
                student.another_direction = int(b[2])+int(b[3])+int(c[2])+int(c[3])

            elif int(b[2]) + int(b[3]) >= 15:
                student.one_direction = b[0]
                student.another_direction = int(a[2])+int(a[3])+int(c[2])+int(c[3])

            elif int(c[2]) + int(c[3]) >= 12 and student.others['SE315'] == '通过':
                student.one_direction = c[0]
                student.another_direction = int(a[2])+int(a[3])+int(b[2])+int(b[3])-3

            else:
                student.another_direction = int(a[2])+int(a[3])+int(c[2])+int(c[3])+int(b[2])+int(b[3])

            list2.append(student)

    #储存数据
    filename = 'static\\' + username + '.txt'
    f = open(filename,'w')
    for person in list1:
        one_person = u''
        one_person += str(person.student_ID) + ',,' + person.name + ',,' + person.department + ',,' + person.major + ',,' + \
            str(person.grade) + ',,' + person.graduate_time + ',,' + person.student_status + ',,' + str(person.failed_number) \
            + ',,' + str(person.center_credits) + ',,' + person.courses_must_to_take + ',,' + person.a_group + ',,' + person.b_group + ',,' +  \
            person.c_group + ',,' + person.d_group + ',,' + person.professional_elective_courses + ',,' + person.enterprise_education_courses \
            + ',,' + person.general_courses + ',,' + person.others
        f.write(one_person+'\n')
    f.close()
    download(list2)
    return list2


def get_data_from_file(username,code_list,name_list):#获取数据
    list2 = []
    list1 = []
    filename = 'static\\' + username + '.txt'
    f = open(filename,'r')
    file_list = f.readlines()
    f.close()
    for one in file_list:
        one = one.decode('utf-8')
        one_list = one.split(',,')
        data_class = data1(one_list[0], one_list[1], one_list[2], one_list[3], one_list[4], one_list[5], one_list[6],
                     one_list[7], one_list[8], one_list[9], one_list[10], one_list[11], one_list[12], one_list[13],
                     one_list[14], one_list[15], one_list[16], one_list[17])
        list1 += [data_class]
    if list1 != []:
        for person in list1:
            student = data2(person.student_ID, person.name, person.department, person.major, person.grade,
                            person.graduate_time, person.student_status, person.failed_number, person.center_credits,
                            person.courses_must_to_take, person.a_group, person.b_group, person.c_group, person.d_group,
                            person.professional_elective_courses, person.enterprise_education_courses,
                            person.general_courses, person.others, '无', '无')
            change(student, code_list)

            #处理one_direction, another_direction两项
            a = student.a_group.replace("\xc2\xa0", " ").split(',')
            b = student.b_group.replace("\xc2\xa0", " ").split(',')
            c = student.c_group.replace("\xc2\xa0", " ").split(',')
            d = student.d_group.replace("\xc2\xa0", " ").split(',')
            tmp = [a,b,c,d]
            for group in tmp:
                if len(group) > 2: 
                    if group[2] == ' ':
                        group[2] = 0
            if int(a[2]) + int(a[3]) >= 15:
                student.one_direction = a[0]
                student.another_direction = int(b[2])+int(b[3])+int(c[2])+int(c[3])

            elif int(b[2]) + int(b[3]) >= 15:
                student.one_direction = b[0]
                student.another_direction = int(a[2])+int(a[3])+int(c[2])+int(c[3])

            elif int(c[2]) + int(c[3]) >= 12 and student.others['SE315'] == '通过':
                student.one_direction = c[0]
                student.another_direction = int(a[2])+int(a[3])+int(b[2])+int(b[3])-3

            else:
                student.another_direction = int(a[2])+int(a[3])+int(c[2])+int(c[3])+int(b[2])+int(b[3])

            list2.append(student)
    download(list2,code_list,name_list)
    return list2
