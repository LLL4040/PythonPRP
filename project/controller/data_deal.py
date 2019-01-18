#-*- coding:utf-8 -*-
from spider import *
from Student import get_and_post
from download import *

def data_deal(list1):#list1是从spider.py接受到的原始数据
    list2 = []

    if list1 != []:
        for person in list1:
            student = data2(person.student_ID, person.name, person.department, person.major, person.grade,
                            person.graduate_time, person.student_status, person.failed_number, person.center_credits,
                            person.courses_must_to_take, person.a_group, person.b_group, person.c_group, person.d_group,
                            person.professional_elective_courses, person.enterprise_education_courses,
                            person.general_courses, person.others, '无', '无')
            student.change()

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
                    if int(group[2]) + int(group[3]) >= int(group[1]):
                        student.one_direction = group[0]
                    elif int(group[2]) + int(group[3]) >= 6:
                        student.another_direction = group[0]

            list2.append(student)

    #get_and_post.add(list2)#储存数据
    download(list2)
    return list2


def get_data_from_model():#从model获取数据
    tmp = get_and_post.show()
    return tmp
