# -*- coding: utf-8 -*-

print('Hello World')

# name = raw_input("按下 enter 键退出，其他任意键显示...\n"
#                    "请输入：")

# print(name)

print(True or False)

# age = raw_input("请输入年龄：")
# age = int(age)

# if age >= 18:
#    print("成年")
# else:
#    print("未成年")

print(10 / 3)
print(10 // 3)

print('哈迪斯'.encode('UTF-8'))

print('年龄：%d,姓名:%s' % (18, '张三'))

list1 = ['a', 'b', 'c']

print(list1)

print(len(list1))

print(list1[0])

print(list1[-1])

list1.append('dd')

print(list1)

list1.insert(2, 'cc')

print(list1)

popVar = list1.pop()

print(popVar)

print(list1)

listCantChange = ('a', 'b', 'c')

print(listCantChange)

print(listCantChange[2])

for x in listCantChange:
    print(x)

count = 0
for x in range(101):
    count = count + x
#    print(count)

for x in range(1, 10):
    for y in range(1, x + 1):
        print('%2d *%2d = %2d ' % (y, x, x * y), end='')
    print()

for x in range(1, 10):
    for y in range(1, 10):
        print('%2d *%2d = %2d ' % (y, x, x * y), end='')
        if x == y:
            break
    print()

dictMap = {'a': 1, 'b': 2}

print(dictMap)

print(dictMap['a'])

for x in dictMap:
    if 'a' in dictMap:
        print('c')
        continue
    print(x)

for x in dictMap:
    print('%s,%s' % (x, dictMap.get(x)))
