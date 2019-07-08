#!/usr/bin/python3
# -*-coding: UTF-8 -*-

print '----------------------------Standard data type----------------------------'
# String
print '--------------String------------------'
var1 = 'hello world'
var2 = 'yang lin'
print (var1[1])
print (var2[3:6])
print (var1[:6] + 'lynn')
print ('e' in var1)
print ('e' not in var1)

print ('My name is %s, and I am %d. %c' % ('lynn', 24, 48))
# print ('address is %p' % ())
print (' '.isspace())

# list
print '--------------list------------------'
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print (list1[0])
print (list2[2:5])
list1[1] = 'lin'
print (list1)
del list2[3]
print list2
print len(list1)
print (list1 + list2)
print (list1 * 3)
print ('lin' in list1)
print ('lin' not in list1)
# for x in list1: print (x, end=' ')
print list1[2]
print list1[-2]
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print (squares)
list3 = [list1, list2]
print list3
# print list3[0][2]
print max(list3)
print min(list3)

# tup
print '--------------tup------------------'
# 元组的元素不能修改，元组可以没有括号或者用小括号
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # 不需要括号也可以
print type(tup1)
tup4 = (50)
print type(tup4)
tup4 = (50,)
print type(tup4)
print tup1[1]
print tup2[0:2]
# 元组中的值不允许修改，但是可以连接组合几个元组
tup5 = tup1 + tup2
print tup5
tup7 = [tup1, tup2]
print tup7
print type(tup7)
tup8 = (tup1, tup2)
print tup8
print type(tup8)
# del tup5[1] # 元组不支持删除其中的元素
# del tup5
# print tup5 # 删除元组后打印的话，会报错找不到该元组
print len(tup1)
# for i in tup1:
#    print i
print tup1[1]
print tup1[-2]
print tup1[-2:]
print tup1[:-2]
print tup1[1:]
print max(tup5)
print min(tup5)
tup6 = tuple(list3)
print list3
print tup6

# dict
print '--------------dict------------------'
# dict的key是唯一的，value则不必
# key的类型必须是一致的，value的可为任意数据类型
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict1 = {'abc': 456};
print dict1
dict2 = {'abc': 123, 98.6: 37}
print dict2
print 'dict2[98.6]: ', dict2[98.6]
dict2[98.6] = 'yanglin'
print dict2
# del dict['Age']
# print dict
dict1.clear()
print dict1
# del dict1
# print dict1
# 字典的值可以使任何python对象——（标准对象、用户定义的对象）
# 键不能是任意对象
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict3 = {'Name': 'zhoujian', 'Age': 100, 'Name': 'yanglin'}
print ("dict3['Name']: ", dict3['Name'])
print len(dict3)
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict4 = {('Name','age'): 'zhoujian'}
print dict4
print len(dict)
print str(dict)
print 'Age' in dict3
print dict.items()
print type(dict.items())
print type((dict.items())[0])
print dict.keys()
print dict.values()
dict.update(dict2)  # 把字典dict2的键/值对更新到dict里
print dict
dict.pop('Name')
print dict

# set
print '--------------set------------------'
# set是一个无序不重复元素的序列
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
set = {1, 2, 2, 4, 5, 6, 7}
print type(set)
set1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print set1
print 'apple' in set1  # 判断元素是否在集合中存在
# set2 = set('abracadabra')
# set3 = set('alacazam')
# print set2
# print set3
a = {x for x in 'abracadabra' if x not in 'abc'}
print a
# s.update( "字符串" ) 与 s.update( {"字符串"} ) 含义不同:
# s.update( {"字符串"} ) 将字符串添加到集合中。
# s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略
a.update('ff')
print a
a.update({'gg'})
print a
a.add('a')  # 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
print a
a.update({1, 3})  # 添加元素，且参数可以是列表，元组，字典等
print a  # set(['a', 1, 'r', 'd', 3])
a.update([1, 4], [5, 6])
print a  # set(['a', 1, 3, 4, 'd', 6, 'r', 5])
# a.remove({1, 3})  # 元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
a.remove(1)
print a
a.discard({1, 3})  # 移除集合中的元素，且如果元素不存在，不会发生错误
print a
a.discard(1)
print a
a.discard(3)
print a
a.pop()  # 随机删除集合中的一个元素
print a

print len(set1)  # 计算几个元素个数
a.clear()  # 清空集合
print a
