#-*- coding: utf-8 -*-
from django.shortcuts import render
from member.models import Member
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def list(request):
    contact_list = Member.objects.all()
    paginator = Paginator(contact_list, 5) # Show 5 contacts per page

    page = request.GET.get('page',1)
    try:
        member_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        member_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        member_list = paginator.page(paginator.num_pages)

    return render(
        request, 
        'member/list.html', 
        {'member_list':member_list},
    )



def insertform(request):
    return render(request, 'member/insertform.html')

def insert(request):
    # post 방식 전송되기 위해서는 form 안에 {% csrf_token %} 작성
    # post방식 전송되는 파라미터추출해서 Member 모델 객체 생성
    mem=Member(
        name=request.POST.get("name"),
        addr=request.POST.get("addr"),
    )
    # DB에 반영
    mem.save()
    # 리다일렉트 이동하라고 응답
    return HttpResponseRedirect('/member/list/')

def delete(request):
    # get 방식 전달되는 삭제할 번호 얻어오기
    #num= request.GET.get("num")
    # 삭제하기
    #mem=Member.objects.get(num=num)
    #mem.delete()
    
    # 위의 작업을 한줄로 표현하면 ...
    Member.objects.get(num=request.GET.get("num")).delete()
    
    #return HttpResponseRedirect("/member/list/")
    return render(
        request,
        'member/alert.html',
        {
            "msg":u"삭제 했습니다.",
            "url":"/member/list/",
        },
    )

def updateform(request):
    # get 방식 전달된 수정할 회원의 번호를 이용해서 회원 정보를 얻어온다.
    member=Member.objects.get(num=request.GET.get("num")) 
    # member 는 dict type 이다.
    return render(
        request,
        'member/updateform.html',
        {"member":member}
    )
def update(request):
    member=Member(
        num=request.POST.get("num"),
        name=request.POST.get("name"),
        addr=request.POST.get("addr"),
    )
    # .save() 메소드는 data 가 있으면 수정 반영, 없으면 insert
    member.save()
    return render(
        request,
        'member/alert.html',
        {"msg":u"수정했습니다.", "url":"/member/list/"},    
    )

