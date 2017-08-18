#-*- coding: utf-8 -*-
from django.contrib import admin
from myapp.models import Message

# Register your models here.

#admin.site.register(Message)

class MessageAdmin(admin.ModelAdmin):
    #관리자 모드에서 보여질 칼럼명 구성하기
    list_display=('id', 'content', 'regdate')
    
admin.site.register(Message, MessageAdmin)
