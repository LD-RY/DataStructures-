'''
    1. 列表：list
        生成列表：+，append,insert(index,item)，列表生成式[i for i in range(n)]
        删：pop()   pop(0)
    2. 字典：dict
        增：
        删：
'''
def test1():
   l = []
   for i in range(1000):
      l = l + [i]
def test2():
   l = []
   for i in range(1000):
      l.append(i)
def test3():
   l = [i for i in range(1000)]
def test4():
   l = list(range(1000))

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("+ ",t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("列表生成式 ",t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list() ",t4.timeit(number=1000), "seconds")



x = list(range(2000000))
pop_zero = Timer("x.pop(0)","from __main__ import x")
print("pop_zero ",pop_zero.timeit(number=1000), "seconds")
x = list(range(2000000))
pop_end = Timer("x.pop()","from __main__ import x")
print("pop_end ",pop_end.timeit(number=1000), "seconds")


insert_end = Timer("x.append(10)","from __main__ import x")
print("append",insert_end.timeit(number=1000),"seconds")

insert_zero = Timer("x.insert(0,10)","from __main__ import x")
print("insert zero",insert_zero.timeit(number=1000),"seconds")



from pythonds.basic.stack import Stack
from pythonds.basic.queue import Queue
from pythonds.basic.deque import Deque

from pythonds.trees import Tree
from pythonds.graphs import Graph



