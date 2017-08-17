#-*- coding: utf-8 -*-

# tuple 타입 = args / # dict 타입 = kwargs
# 어떤 인자의 형태도 받아줄 수 있는 함수
def test(*args, **kwargs):
    print args
    print kwargs
    print "--- test() ---"

def test2(**kwargs):
    print kwargs
    print "--- test2() ---"

def auth(func):
    def wrapper(*args, **kwargs):
        # decorator 가 적용된 함수에 전달된 인자를 얻어올 수 있다.
        print args, kwargs
        # kwargs 는 dict type 이므로 kwargs["key"] 형태로 참조
        print kwargs["name"], " auth !"
        func(*args, **kwargs)
        print kwargs["name"], " Success !"
    return wrapper

@auth
def updateUser(name):
    print name,u"업데이트 합니다."
@auth
def deleteUser(name):
    print name,u"삭제합니다"

if __name__ == '__main__':

    # test(1)
    # test(1,2)
    #test("a","b","c")
    #test(name="gura")
    #test(isMan=True)
    #test(name="monkey",isMan=False)
    #test("a","b",name="cat",isMan=True)
    test2(name="monkey")
    #updateUser(name="gura")
    #deleteUser(name="monkey")