#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def solution(line):
    a, target, k = line.strip().split(' ')
    a = a.split(',')
    for i in range(len(a)):
        a[i] = int(a[i])
    target = int(target)
    k = int(k)
    ans = []
    sumof(a, target, k, 0, False, ans)



def sumof(a, target, k, i, flag, ans):
    if i == len(a) or target <= 0 or flag or k <= 0:
        return
    if target == a[i] and k == 1:
        ans.append(a[i])
        flag = True
        print ans, target, k
        ans.pop()
    ans.append(a[i])
    sumof(a, target-a[i], k-1, i+1, flag, ans)
    ans.pop()
    sumof(a, target, k, i+1, flag, ans)



s = '1,9,2,8,3,7,4,6,5 20 5'
print(solution(s))