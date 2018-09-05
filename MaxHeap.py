#!/usr/bin/python
#  -*- coding: UTF-8 -*-


class MaxHeap():  # 堆是完全二叉树(有右儿子就一定有左儿子)，但不是满二叉树
    def __init__(self, arr):  # init a maxHeap
        self.data = arr
        self.count = len(self.data)
        i = self.count >> 1 - 1  # count右移  相当于除2   右移一位再减1 则为
        while i >= 0:
            self.shiftdown(i)
            i -= 1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self, item):  # 插入
        self.data.append(item)
        self.count += 1
        self.shiftup(self.count)

    def shiftup(self, count):  # insert元素后，可能不再是大顶堆，该函数把新元素放到满足堆是大顶堆的位置
        while count > 1 and self.data[count/2-1] < self.data[count-1]:  #
            self.data[count/2-1], self.data[count-1] = self.data[count-1], self.data[count/2-1]  # 交换两个值
            count = count / 2  #

    def extractmax(self):  # 取最大的一个数出来
        if self.count > 0:
            res = self.data[0]
            self.data[0], self.data[self.count-1] = self.data[self.count-1], self.data[0]
            self.data = self.data[:-1]
            self.count -= 1
            self.shiftdown(0)
            return res

    def shiftdown(self, count):  # 初始化时，
        while 2*count+1 < self.count:  # 左儿子的索引仍然小于堆的长度
            j = 2*count+1  # j等于左儿子的索引
            if j+1 < self.count:  # 右儿子的索引仍然小于堆的长度
                if self.data[j] < self.data[j+1]:  # 若左儿子的值小于右儿子的值，两个儿子中最大值为右儿子，索引为j + 1；否则两个儿子中最大值为左儿子，索引为j，不变
                    j += 1
            if self.data[count] > self.data[j]:  # 若父亲节点的值大于两个儿子中最大值节点的值，不操作；否则，交换父亲节点和儿子节点中值最大的节点
                break
            # print self.data[count], self.data[j], count, j
            self.data[count], self.data[j] = self.data[j], self.data[count]
            count = j


a =  MaxHeap([0,1,2,3,4,5,6])
print a.data
a.insert(7)
print a.data