#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 一个数组的最长连续和

def solution(line):
    s = line.strip().split(',')
    temp = 0
    ans = -10000000000000
    for i in s:
        temp = int(i) if temp < 0 else temp + int(i)
        if temp > ans:
            ans = temp
        '''
        temp = temp + int(i)
        if temp >= 0 and temp > ans:
            ans = temp
        if temp < 0:
            temp = int(i)
        print temp
        '''
    return ans


def main():
    s = "-2,11,-4,13,-5,-2"
    print solution(s)


if __name__ == "__main__":
    main()