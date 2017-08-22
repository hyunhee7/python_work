#-*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    
    # templates/index.html 을 읽어서 출력하도록 
    return render(request, 'index.html')
