#-*- coding: utf-8 -*-
'''
    여러 줄 주석입니다.
'''

"""
    여러 줄 주석입니다.
"""

# 한 줄 주석입니다.

# Data Type 확인하기
print 1 # int type
print 1+1 
print type(1) 

print type(10.1) # float type

print type(True) # bool type
print type(False) 

print type('abcd') # str type
print type("abcd") 

print type(u"한글입니다.") # unicode type 
print type(u"김구라 abcd")

print type([]) # list type(python에서 배열)
print type(["aa", "bb", "cc"])

print type({}) # dict type(object)
print type({"num":1, "name":"gura", "isMan":True})

print type({10, 20, 30}) #set type
print type({"aa", "bb", "cc"})

print type(None) #None type

#myFunction 이라는 이름의 함수 만들기
def myFunction():
    print u"하나"
    print u"두울"
    print u"세엣"
    print u"myFunction 이 리턴됩니다."
   
#myFunction 함수 호출하기
myFunction()   
    
print u"Step01_DataType 모듈로 들어온 실행순서가 종료됩니다."