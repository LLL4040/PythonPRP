#-*- coding:utf-8 -*-
from models import DataModel

def add(list1):#向数据库中增添数据
    DataModel.objects.all().delete()
    for person in list1:
        student = DataModel(student_ID = person.student_ID,
                            name = person.name,
                            department = person.department,
                            major = person.major,
                            grade = person.grade,
                            graduate_time = person.graduate_time,
                            student_status = person.student_status,
                            failed_number = person.failed_number,
                            center_credits = person.center_credits,
                            courses_must_to_take = person.courses_must_to_take,
                            general_courses = person.general_courses,
                            others = person.others)
        student.save()
    return
    
def show():#从数据库中向外展示数据
    list2 = DataModel.objects.all()
    return list2