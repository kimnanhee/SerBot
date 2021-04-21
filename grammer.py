import random, time, os
'''
random 파일 찾기
'''

def randint_test():
    num = [0 for _ in range(10)]
    print(num)
    for i in range(1000):
        num[random.randint(1, 10)-1] += 1
    print(num)

def rand_test(start, end, count=10):
    ret = {start+i : 0 for i in range(end-start+1)}
    print(ret)

    for _ in range(count):
        ret[random.randint(start, end)] += 1
    return ret

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b 

def div(a, b):
    return a//b

def calc_test():
    x = int(input())
    op = input()
    y = int(input())

    fun_tbl = {"+":add, "-":sub, "*":mul, "/":div}
    fun_tbl[op](x, y)

class NH(object):
    def __init__(self):
        self.a = None # 인스턴스 변수
        print("call NH construct")

    def foo(self, a):
        self.a = a
        print("call foo", self.a)

    def __del__(self):
        print("call NH dectuct")

def nh():
    def boo():
        return 1
    return boo

if __name__ == "__main__":
    print(os.path)
    # randint_test()
    # ret = rand_test(10, 25, count=1000)
    # print(ret)
    # nh = NH()
    # nh.foo("12")
    # time.sleep(1)
    my.a = 10