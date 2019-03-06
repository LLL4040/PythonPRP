# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from PIL import Image
import time
import urllib
from bs4 import BeautifulSoup

class data1:#生成data实例
    def __init__(self, student_ID, name, department, major, grade, graduate_time, student_status,
                 failed_number, center_credits, courses_must_to_take, a_group, b_group, c_group, d_group,
                 professional_elective_courses, enterprise_education_courses, general_courses, others):
        self.student_ID = student_ID#学号
        self.name = name#姓名
        self.department = department#学院
        self.major = major#专业
        self.grade = grade#年级
        self.graduate_time = graduate_time#毕业时间
        self.student_status = student_status#学籍状态
        self.failed_number = failed_number#不及格门数
        self.center_credits = center_credits#目前修读核心课程学分
        self.courses_must_to_take = courses_must_to_take#暂未修读课程
        self.a_group = a_group
        self.b_group = b_group
        self.c_group = c_group
        self.d_group = d_group
        self.professional_elective_courses = professional_elective_courses#专业选修课
        self.enterprise_education_courses = enterprise_education_courses#企业教育课
        self.general_courses = general_courses#通识及以下栏目
        self.others = others#必修的选修课

class data2(data1):#返回给manager的数据实例
    def __init__(self, student_ID, name, department, major, grade, graduate_time, student_status,
                 failed_number, center_credits, courses_must_to_take, a_group, b_group, c_group, d_group,
                 professional_elective_courses, enterprise_education_courses, general_courses, others,
                 one_direction, another_direction):
        data1.__init__(self,student_ID,name,department,major,grade,graduate_time,student_status,
                 failed_number,center_credits,courses_must_to_take,a_group,b_group,c_group,d_group,
                 professional_elective_courses,enterprise_education_courses,general_courses,others)#原始数据初始化
        self.one_direction = one_direction#修读完某一方向
        self.another_direction = another_direction#其他方向学分

def data_deal(list_origin,graduate_time):
    list_dealing = []
    for data in list_origin:
        data_dealing = data.find(attrs={"id":"lbXH"})#学号
        student_ID = data_dealing.string
        
        data_dealing = data.find(attrs={"id":"lbXm"})#姓名
        name = data_dealing.string
        name = ''.join([name]).encode('utf-8')
        
        data_dealing = data.find(attrs={"id":"lbYx"})#学院
        department = data_dealing.string
        
        data_dealing = data.find(attrs={"id":"lbZy"})#专业
        major = data_dealing.string

        data_dealing = data.find(attrs={"id":"lbNj"})#年级
        grade = int(data_dealing.string)

        data_dealing = data.find(attrs={"id":"lbXjzt"})#学籍状态
        student_status = data_dealing.string

        data_dealing = str(data.find(attrs={"id":"dgBX1"})).decode('utf-8')#不及格门数
        failed_data_list = data_dealing.split('tr')
        failed_data = []
        for i in failed_data_list:
            if '需要重修或补考，务必关注！' in i:
                failed_data += [i] 
        failed_number = ''
        for j in failed_data:
            failed_list = j.split('td')
            failed_number = failed_number + '、' + failed_list[3][1:-2]
        failed_number = failed_number[1:]

        data_dealing = data.find(attrs={"id":"lbBxxf2"})#目前修读核心课程学分
        center_credits = int(data_dealing.string)

        data_dealing = data.find(attrs={"id":"dgBX3"})#暂未修读课程
        courses = data_dealing.findAll(attrs={"class":"dgItemStyle"})
        courses += data_dealing.findAll(attrs={"class":"dgAItemStyle"})
        courses_must_to_take=''
        for i in courses:
            str_tmp = str(i)[str(i).index('<td>')+4:]
            str_tmpe = str_tmp[str_tmp.index('<td>')+4:]
            x = str_tmpe.index('</td>')
            courses_must_to_take = courses_must_to_take + '、' + str_tmpe[:x]
        courses_must_to_take = courses_must_to_take[3:]

        data_dealing = data.find(attrs={"id":"dgXX1"})#限选模块
        courses = data_dealing.findAll(attrs={"class":"dgItemStyle"})
        courses += data_dealing.findAll(attrs={"class":"dgAItemStyle"})
        a_group = ''
        str_tmp1 = str(courses[0])[str(courses[0]).index('<td>')+4:]
        a_group = a_group + str_tmp1[:str_tmp1.index('</td>')]+','
        str_tmp1 = str_tmp1[str_tmp1.index('<td>')+4:]
        str_tmp2 = str_tmp1[str_tmp1.index('<td>')+4:]
        a_group = a_group + str_tmp2[:str_tmp2.index('</td>')]+','
        str_tmp3 = str_tmp2[str_tmp2.index('<td>')+4:]
        a_group = a_group + str_tmp3[:str_tmp3.index('</td>')]+','
        str_tmp4 = str_tmp3[str_tmp3.index('<td>')+4:]
        a_group = a_group + str_tmp4[:str_tmp4.index('</td>')]
        
        c_group = ''
        str_tmp1 = str(courses[1])[str(courses[1]).index('<td>')+4:]
        c_group = c_group + str_tmp1[:str_tmp1.index('</td>')]+','
        str_tmp1 = str_tmp1[str_tmp1.index('<td>')+4:]
        str_tmp2 = str_tmp1[str_tmp1.index('<td>')+4:]
        c_group = c_group + str_tmp2[:str_tmp2.index('</td>')]+','
        str_tmp3 = str_tmp2[str_tmp2.index('<td>')+4:]
        c_group = c_group + str_tmp3[:str_tmp3.index('</td>')]+','
        str_tmp4 = str_tmp3[str_tmp3.index('<td>')+4:]
        c_group = c_group + str_tmp4[:str_tmp4.index('</td>')]

        b_group = ''
        str_tmp1 = str(courses[2])[str(courses[2]).index('<td>')+4:]
        b_group = b_group + str_tmp1[:str_tmp1.index('</td>')]+','
        str_tmp1 = str_tmp1[str_tmp1.index('<td>')+4:]
        str_tmp2 = str_tmp1[str_tmp1.index('<td>')+4:]
        b_group = b_group + str_tmp2[:str_tmp2.index('</td>')]+','
        str_tmp3 = str_tmp2[str_tmp2.index('<td>')+4:]
        b_group = b_group + str_tmp3[:str_tmp3.index('</td>')]+','
        str_tmp4 = str_tmp3[str_tmp3.index('<td>')+4:]
        b_group = b_group + str_tmp4[:str_tmp4.index('</td>')]
        
        professional_elective_courses = ''
        '''str_tmp1 = str(courses[2])[str(courses[2]).index('<td>')+4:]
        professional_elective_courses = professional_elective_courses + str_tmp1[:str_tmp1.index('</td>')]+','
        str_tmp1 = str_tmp1[str_tmp1.index('<td>')+4:]
        str_tmp2 = str_tmp1[str_tmp1.index('<td>')+4:]
        professional_elective_courses = professional_elective_courses + str_tmp2[:str_tmp2.index('</td>')]+','
        str_tmp3 = str_tmp2[str_tmp2.index('<td>')+4:]
        professional_elective_courses = professional_elective_courses + str_tmp3[:str_tmp3.index('</td>')]+','
        str_tmp4 = str_tmp3[str_tmp3.index('<td>')+4:]
        professional_elective_courses = professional_elective_courses + str_tmp4[:str_tmp4.index('</td>')]'''

        '''str_tmp1 = str(courses[3])[str(courses[3]).index('<td>')+4:]
        b_group = b_group + str_tmp1[:str_tmp1.index('</td>')]+','
        str_tmp1 = str_tmp1[str_tmp1.index('<td>')+4:]
        str_tmp2 = str_tmp1[str_tmp1.index('<td>')+4:]
        b_group = b_group + str_tmp2[:str_tmp2.index('</td>')]+','
        str_tmp3 = str_tmp2[str_tmp2.index('<td>')+4:]
        b_group = b_group + str_tmp3[:str_tmp3.index('</td>')]+','
        str_tmp4 = str_tmp3[str_tmp3.index('<td>')+4:]
        b_group = b_group + str_tmp4[:str_tmp4.index('</td>')]'''

        d_group = ''
        '''str_tmp1 = str(courses[4])[str(courses[4]).index('<td>')+4:]
        d_group = d_group + str_tmp1[:str_tmp1.index('</td>')]+','
        str_tmp1 = str_tmp1[str_tmp1.index('<td>')+4:]
        str_tmp2 = str_tmp1[str_tmp1.index('<td>')+4:]
        d_group = d_group + str_tmp2[:str_tmp2.index('</td>')]+','
        str_tmp3 = str_tmp2[str_tmp2.index('<td>')+4:]
        d_group = d_group + str_tmp3[:str_tmp3.index('</td>')]+','
        str_tmp4 = str_tmp3[str_tmp3.index('<td>')+4:]
        d_group = d_group + str_tmp4[:str_tmp4.index('</td>')]'''

        enterprise_education_courses = ''
        '''str_tmp = (str(courses[5])).decode('utf-8')
        str_tmp1 = str_tmp[str_tmp.index('<td>')+4:]
        enterprise_education_courses = enterprise_education_courses + str_tmp1[:str_tmp1.index('</td>')]+','
        str_tmp1 = str_tmp1[str_tmp1.index('<td>')+4:]
        str_tmp2 = str_tmp1[str_tmp1.index('<td>')+4:]
        enterprise_education_courses = enterprise_education_courses + str_tmp2[:str_tmp2.index('</td>')]+','
        str_tmp3 = str_tmp2[str_tmp2.index('<td>')+4:]
        enterprise_education_courses = enterprise_education_courses + str_tmp3[:str_tmp3.index('</td>')]+','
        str_tmp4 = str_tmp3[str_tmp3.index('<td>')+4:]
        enterprise_education_courses = enterprise_education_courses + str_tmp4[:str_tmp4.index('</td>')]'''

        data_dealing = data.find(attrs={"id":"dgTsk1"})#人文、社科、自然
        courses = data_dealing.findAll(attrs={"class":"dgItemStyle"})
        courses += data_dealing.findAll(attrs={"class":"dgAItemStyle"})
        general_courses = ''
        for i in courses:
            course_tmp = str(i)
            if '√' in course_tmp:
                general_courses = general_courses
            else:
                course_tmp1 = course_tmp[course_tmp.index('<td>')+4:]
                g_name = course_tmp1[:course_tmp1.index('</td>')]
                course_tmp2 = course_tmp1[course_tmp1.index('<td>')+4:]
                number_ask = float(course_tmp2[:course_tmp2.index('</td>')])
                course_tmp3 = course_tmp2[course_tmp2.index('<td>')+4:]
                course_tmp3 = course_tmp3[course_tmp3.index('<td>')+4:]
                number_get = float(course_tmp3[:course_tmp3.index('</td>')])
                if number_ask > number_get :
                    number_lack = number_ask - number_get
                    if g_name == '自然科学与工程技术':
                        g_name = '自科'
                    elif g_name == '人文学科':
                        g_name = '人文'
                    elif g_name == '社会科学':
                        g_name = '社科'
                    general_courses =general_courses + '、' + g_name + '缺' + str(number_lack)

        data_dealing = data.find(attrs={"id":"lbCS1"})#计算机
        number_ask = int(data_dealing.string)
        data_dealing = data.find(attrs={"id":"lbCS2"})
        number_get = int(data_dealing.string)
        if number_ask > number_get:
            general_courses = general_courses + '、' + '计算机缺' + str(number_ask-number_get)

        data_dealing = data.find(attrs={"id":"lbPE1"})#体育
        number_ask = int(data_dealing.string)
        data_dealing = data.find(attrs={"id":"lbPE2"})
        number_get = int(data_dealing.string)
        if number_ask > number_get:
            general_courses = general_courses + '、' + '体育缺' + str(number_ask-number_get)

        data_dealing = data.find(attrs={"id":"lbTH1"})#两课
        number_ask = int(data_dealing.string)
        data_dealing = data.find(attrs={"id":"lbTH2"})
        number_get = int(data_dealing.string)
        if number_ask > number_get:
            general_courses = general_courses + '、' + '两课缺' + str(number_ask-number_get)

        data_dealing = str(data)#英语
        data_tmp = data_dealing[data_dealing.index('英语成绩情况'):]
        
        def find_n_sub_str(src, sub, pos, start):
            index = src.find(sub, start)
            if index != -1 and pos > 0:
                return find_n_sub_str(src, sub, pos - 1, index + 1)
            return index
        
        index = find_n_sub_str(data_tmp,'</td>',5,0)
        data_tmp1 = data_tmp[:index]
        if '√' in data_tmp1 :
            general_courses = general_courses
        else :
            index2 = find_n_sub_str(data_tmp1,'</td>',1,0)
            index1 = find_n_sub_str(data_tmp1,'>',2,0)
            general_courses = general_courses +'、'+ data_tmp1[index1+1:index2]
            
        general_courses = general_courses[3:]


        data_dealing = data.find(attrs={"id":"dgGxh2"})#必修的选修课
        courses = data_dealing.findAll(attrs={"class":"dgItemStyle"})
        courses += data_dealing.findAll(attrs={"class":"dgAItemStyle"})
        others = ''
        
        for course in courses:
            course = str(course)
            one = ''
            one = one + course[course.index('<td>')+4:course.index('</td>')]
            one = one + ',' + course[find_n_sub_str(course,'<td>',1,0)+4:find_n_sub_str(course,'</td>',1,0)]
            one = one + ',' + course[find_n_sub_str(course,'>',11,0)+1:find_n_sub_str(course,'</td>',5,0)]
            one = one + ';'
            others = others + one
        data_dealing = data.find(attrs={"id":"dgBX1"})#必修课
        courses = data_dealing.findAll(attrs={"class":"dgItemStyle"})
        courses += data_dealing.findAll(attrs={"class":"dgAItemStyle"})
        
        for course in courses:
            course = str(course)
            one = ''
            one = one + course[course.index('<td>')+4:course.index('</td>')]
            one = one + ',' + course[find_n_sub_str(course,'<td>',1,0)+4:find_n_sub_str(course,'</td>',1,0)]
            one = one + ',' + course[find_n_sub_str(course,'>',11,0)+1:find_n_sub_str(course,'</td>',5,0)]
            one = one + ';'
            others = others + one
        data_dealing = data.find(attrs={"id":"dgXX2"})#必修的选修课
        courses = data_dealing.findAll(attrs={"class":"dgItemStyle"})
        courses += data_dealing.findAll(attrs={"class":"dgAItemStyle"})
        
        for course in courses:
            course = str(course)
            one = ''
            one = one + course[find_n_sub_str(course,'<td>',1,0)+4:find_n_sub_str(course,'</td>',1,0)]
            one = one + ',' + course[find_n_sub_str(course,'<td>',2,0)+4:find_n_sub_str(course,'</td>',2,0)]
            one = one + ',' + course[find_n_sub_str(course,'<td>',6,0)+4:find_n_sub_str(course,'</td>',6,0)]
            one = one + ';'
            others = others + one
        data_class = data1(student_ID, name, department, major, grade, graduate_time, student_status,
                     failed_number, center_credits, courses_must_to_take, a_group, b_group, c_group, d_group,
                     professional_elective_courses, enterprise_education_courses, general_courses, others)
        list_dealing += [data_class] 
    return list_dealing

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://i.jwc.sjtu.edu.cn/EduPlate/SEduService/StuStatusManage/GraduationAudit/GraduationAudit.aspx?MID=179702&ID=-1&STR=&642606892")
    driver.save_screenshot('static\\photo.png')
    element = driver.find_element_by_xpath("//div[@class='input-control captcha-input']/img")
    left = int(element.location['x'])*1.5
    top = int(element.location['y'])*1.5
    right = int(element.location['x'] + element.size['width'])*1.5
    bottom = int(element.location['y'] + element.size['height'])*1.5
    i = Image.open("static\\photo.png")
    frame4 = i.crop((left, top, right, bottom))
    frame4.save('static\\save.png')
    return driver

def get_data(driver, user, password, icode):
    driver.find_element_by_id("user").send_keys(user)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("captcha").send_keys(icode)
    driver.find_element_by_id("form-input").submit()
    time.sleep(1)
    if driver.title != '毕业资格审核':
        return False
    academy = driver.find_element_by_xpath("//*[@id='ddlYX']")
    Select(academy).select_by_value("03000")
    time.sleep(1)
    major = driver.find_element_by_xpath("//*[@id='ddlZY']")
    Select(major).select_by_value("0806050037")
    state = driver.find_element_by_xpath("//*[@id='ddlSHStatus']")
    Select(state).select_by_value("0")
    select_all = driver.find_element_by_xpath("//*[@id='ddlFY']")
    Select(select_all).select_by_value("1")

    ok = driver.find_element_by_id("BtnQuery").click()

    list1 = driver.find_elements_by_class_name("dgItemStyle")
    list2 = driver.find_elements_by_class_name("dgAItemStyle")
    number = len(list1)+len(list2)
    
    list_of_data = []

    data_dealing = driver.find_element_by_xpath("//*[@id='dgSet']/tbody/tr[2]/td[8]")#毕业时间
    graduate_time = data_dealing.text
    driver.set_script_timeout(0)
    for i in xrange(number): #number
        page = driver.find_element_by_xpath("//*[@id='dgSet']/tbody/tr[%d]/td[13]"%(2+i)).click()
        handles = driver.window_handles
        driver.switch_to_window(handles[1])
        soup_data = BeautifulSoup(driver.page_source,"html.parser")
        list_of_data += [soup_data]
        driver.close()
        driver.switch_to_window(handles[0])
    data_list = data_deal(list_of_data,graduate_time)

    driver.close()

    return data_list
