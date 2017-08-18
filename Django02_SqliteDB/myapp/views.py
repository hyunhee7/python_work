#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from myapp.models import Message

# Create your views here.

# myapp.views.py

# /message/hello 요청에 대한 응답
def hello(request):
    return HttpResponse("hello ok!")

def list(request):
    result = Message.objects.all() # list type
    
    for item in result:
        print item.id
        print item.content
        print item.regdate
        
    print result
    
    return render_to_response("list.html", {"list":result})