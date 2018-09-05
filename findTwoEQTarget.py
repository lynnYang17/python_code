#!/usr/bin/python3
# -*-coding: UTF-8 -*-


def solution(line):
    a, sum = line.strip().split(' ')
    dict1 = {}
    a = a.strip().split(',')
    sort(a)
    # print a


def sort(line):
    l = len(line)
    for i in range(0, l, 1):
        for j in range(0, l - i - 1):
            if int(line[j]) > int(line[j + 1]):
                temp = int(line[j])
                line[j] = int(line[j + 1])
                line[j + 1] = temp
    for k in range(0, l):
        line[k] = int(line[k])
    return line


def sum(a, sum):
    l = len(a)
    res = {}
    for i in range(0, l, 1):
        for j in range(-1, l, -1):
            if a[j] == sum - a[i]:
                dict
                

s = '1,9,2,8,3,7,4,6,5 10'
# a = '1, 9, 2, 8, 3, 7, 4, 6, 5'
print solution(s)
