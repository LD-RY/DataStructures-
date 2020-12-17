'''
    递归也是一种迭代
    什么是递归？
    一、递归的定义
        递归是一种解决问题的方法，他把一个问题分解为越来越小的子问题，
        直到问题的规模小到可以被很简单直接解决
        通常为了达到分解,在递归过程中要引入一个***调用自身的函数***

    二、递归的三大定律
        1. 递归算法必须有个基本结束条件（长度为1的列表） 
        2. 递归算法必须改变自己的状态并向基本结束条件演进 
        3. 递归算法必须递归地调用自身（核心）

'''
import time
# 计算[1,2,3,4,5,6,7] 的和
# def sum(aList):
#     result = 0
#     for i in range(len(aList)):
#         result += aList[i]
#     return result

# aList = [1,2,3,4,5,6,7]
# print(sum(aList))





# 递归方法
# 最小条件 aList[0] + sumRec(aList[1:])

aList = [1,2,3,4,5,6,7]
def sumRec(aList):
    if len(aList) == 1:
        return aList[0]
    return aList[0] + sumRec(aList[1:])

start_time = time.time()
for i in range(100000):
    sumRec(aList)
end_time = time.time()

print(end_time-start_time)



'''
四、递归  LeetCode 第405题
        给定一个整数，编写一个算法将这个数转换为十六进制数。
        对于负整数，我们通常使用补码运算方法
        给定一个整数，转换成任意进制表示的字符串格式
        769  转换成  字符串 769
        str = "0123456789ABCDEF"
        769/10    =   76  余  9
        76/10     =   7   余  6
        7/10      =   0   余  7
        str[9] + str[6] + str[7]

    16进制的301 转换成10进制
    3*16^2 + 0 + 1*16^0 = 769

    八进制的1401 转换成10进制
    1*8^3 +4*8^2 + 0 + 1*8^0

    十进制的14 转换成2进制
    7 0
    3 1
    1 1
    1110
    1*2^3 + 1*2^2 + 1*2^1 + 0*2^0 


'''

def to_str(n,base):
    convert_str='0123456789ABCDEF'
    if n < base:
        return convert_str[n]
    else:
        return to_str(n//base,base) + convert_str[n%base]

print(to_str(769,10))
print(to_str(769,8))
print(to_str(769,16))
print(to_str(769,2))
















