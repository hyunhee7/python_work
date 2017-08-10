#-*- coding: utf-8 -*-
from deco.myDeco import HelloBye, Auth


@HelloBye
def test1():
    print "test1() called"
@Auth
def test2():
    print "test2() called"
if __name__ == '__main__':
    test1()
    test2()