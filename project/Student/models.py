# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

class DataModel(models.Model):
    student_ID = models.CharField(max_length = 12)
    name = models.CharField(max_length = 30)
    department = models.CharField(max_length = 20)
    major = models.CharField(max_length = 20)
    grade = models.IntegerField()
    graduate_time = models.CharField(max_length = 10)
    student_status = models.CharField(max_length = 4)
    failed_number = models.IntegerField()
    center_credits = models.IntegerField()
    courses_must_to_take = models.CharField(max_length = 400)
    general_courses = models.CharField(max_length = 50)
    one_direction = models.CharField(max_length = 50)
    another_direction = models.CharField(max_length = 50)
    others = models.CharField(max_length = 1000)

class UserLogin(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    icode = forms.CharField(label='验证码', max_length=10)

class CrossNumber(forms.Form):
    num = forms.IntegerField(label='跨方向门数')

class ExtraClass(forms.Form):
    ID = forms.CharField(label='课程代码', max_length=10)
    Name = forms.CharField(label='课程名称', max_length=100)
    Credit = forms.IntegerField(label='学分')
        
        