#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# ------ by lynn -------


def solution(line):
    a = line.strip().split(',')
    # 初始化一个大顶堆，时间复杂度O(n/2lgn).
    # 初始化：cnt=len(a)，i=cnt/2-1,i--,i=0结束，每一步处理一个节点，
    # 判断该节点是否比左儿子or左儿子和右儿子中最大值大，如果大，不操作；如果小，和最大的儿子交换
    # 成为大顶堆(堆是一个完全二叉树)
    a = [int(i) for i in a]
    cnt = len(a)
    i = cnt/2 - 1
    while i >= 0:
        k = i
        while 2 * k + 1 < cnt:
            j = 2*k + 1
            if j + 1 < cnt:
                if a[j] < a[j + 1]:
                    j += 1
            if a[k] > a[j]:
                break  # 父亲节点满足条件后，下标为i的节点处理完毕，不需要再继续处理下边的，所以i=j操作也不需要
            a[k], a[j] = a[j], a[k]
            k = j
        i -= 1
    print a

    # 开始排序(时间复杂度：O(nlgn))
    # 每次取出根节点a[0]，和最后一个节点交换，然后cnt-1开始将剩余的元素建为大顶堆
    while cnt >= 1:
        a[0], a[cnt - 1] = a[cnt - 1], a[0]
        cnt -= 1
        i = 0
        k = i
        while 2 * k + 1 < cnt:
            j = 2 * k + 1
            if j + 1 < cnt:
                if a[j] < a[j + 1]:
                    j += 1
            if a[k] > a[j]:
                break
            a[k], a[j] = a[j], a[k]
            k = j
    return a


s = '1,9,2,8,3,7,4,6,5'
s1 = '9,17,3,6,2,8,0'
print solution(s)
print solution(s1)
# 总时间复杂度为 n/2lgn + nlgn ——> O(nlgn)
