#-*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')

def game(request):
    return render(request, 'game.html')

def include(request):
    return render(request, 'includeTest.html')