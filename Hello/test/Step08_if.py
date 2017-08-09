#-*- coding: utf-8 -*-

'''
    - if 문 사용하기
    1. 조건부로 특정 블럭을 수행 하고자 할 때 사용
    2. 들여쓰기로 특정 블럭을 구성한다.
'''

# 단일 if문

if True:
    print "ok 1"
    print "ok 2"

if False:
    print "ok 1"
    print "ok 2"    
   
isWait=True

# 조건부 수행
if isWait:
    print "wait!"
    print "wait!"
    print "wait!"
    
# 양자 택일
num=10

if num%2==0 :
    print u"{} 은 짝수 입니다.".format(num)
else:
    print u"{} 은 홀수 입니다.".format(num)
    
# 다중 if 문
jumsu=85
if jumsu >= 90 :
    print u"{} 점은 수입니다".format(jumsu)
elif jumsu >= 80 :
    print u"{} 점은 우입니다".format(jumsu)
elif jumsu >= 70 :
    print u"{} 점은 미입니다".format(jumsu)
elif jumsu >= 60 :
    print u"{} 점은 양입니다".format(jumsu)
else:
    print u"{} 점은 가입니다".format(jumsu)   
    
# 참고 (3항 연산)
isMan = True
result = u"남자 입니다." if isMan else u"여자입니다."
print "isMan :", result

result2 = None
if isMan:
    result2=u"남자 입니다."
else:
    result2=u"여자 입니다."
    
print "isMan: ", result
    
    
print u"Step01_if 모듈의 실행 순서가 종료 됩니다."
