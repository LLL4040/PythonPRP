# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from controller import manager

def homepage(request):
    return render(request, 'homepage.html')