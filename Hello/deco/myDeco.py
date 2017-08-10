#-*- coding: utf-8 -*-

'''
    deco 패키지의 myDeco.py 파일에
    HelloBye 데코레이터 클래스 정의하기
'''
    
# decorator 역할을 할 class 정의하기
class HelloBye:
    #생성자
    def __init__(self,f):
        # 인자로 전달된 함수를 func 라는 필드에 저장하기
        self.func=f
    #객체를 call 했을 때 호출되는 메소드
    def __call__(self, *args, **kwargs):
        print "hello"
        self.func(*args, **kwargs)
        
        #멤버 메소드 호출하기
        self.sing()
        self.dance()
        print "bye!"

    def sing(self):
        print u"노래를 불러요"
        
    def dance(self):
        print u"춤을 춰요"
        
class Auth:
    #생성자
    def __init__(self,f):
        # 인자로 전달된 함수를 func 라는 필드에 저장하기
        self.func=f
    #객체를 call 했을 때 호출되는 메소드
    def __call__(self, *args, **kwargs):
        print "인증 작업을 해요"
        self.func(*args, **kwargs)        
        print "정상 처리 되었습니다"