#-*- coding: utf-8 -*-


# 함수에 전달받는 인자의 default 값을 지정할 수도 있다.

def test(num=0):
    print "num:", num
    
test()
test(999)
print"00------------"
def test2(num=0, name=u"아무게", isMan=True, addr=u"어디게"):
    print "num:", num
    print "name:", name
    print "isMan:", isMan
    print "addr:", addr
    
test2(num=99,name=u"김구라")
print"----------"
test2(1,u"오",False)
print"----------"
test2(2,u"해골",True)