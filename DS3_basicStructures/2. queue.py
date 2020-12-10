'''
    什么是队列：队列是一系列元素的集合，新元素的加入在队列的一端，这一段叫做‘队尾(rear)’,
        已有元素的移出发生在队列的另一端,叫做‘队首(front)’
        ----------------------------
    rear                             front
        ----------------------------

    特点：先进先出(FIFO)  first in first out
    抽象数据类型(ADT)
        Queue():创建一个空队列对象，无需参数，返回空的队列
        enqueue(item):将数据项添加到队尾
        dequeue():从队首移除数据项，无需参数，返回值为队首数据项
        isEmpty()测试队列是否为空，无需参数，返回值为布尔值
        size():返回队列中的数据项的个数，无需参数
'''
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(Self):
        return self.items == []

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")

print(q.size())
print(q.dequeue())

print(q.size())


'''
    马铃薯游戏(击鼓传花)，选定一个人作为开始的人，数到num个人，此人淘汰
    ['零','一','二','三','四','五','六','七','八','九']   七
    ['八','九','零','一','二','三','四','五','六']    五
    ['六','八','九','零','一','二','三','四']    四
    ['六','八','九','零','一','二','三']    六
    ['八','九','零','一','二','三']    九
    ['零','一','二','三','八']    二
    ['三','八','零','一']    一
    ['三','八','零']    八
    ['零','三']    三
    ['零']
'''
from pythonds.basic.queue import Queue

name_list = ['零','一','二','三','四','五','六','七','八','九']
num = 7

def send_flowers(name_list,num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        for i in range(num):
            # 把移除的前六个人重新放入队伍
            simqueue.enqueue(simqueue.dequeue()) 
        print(simqueue.dequeue())
    return simqueue.dequeue()

send_flowers(name_list,num)














