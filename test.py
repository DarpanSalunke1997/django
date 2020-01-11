#(20)
# x = 1
# y = "2"
# z = 3
#
# sum = 0
# for i in (x,y,z):
#     if isinstance(i,int):
#         sum += i
# print(sum)

#(19)
# class A:
#     def __init__(self,a,b,c):
#         self.x = a+b+c
#
# a = A(1,2,3)
# b = getattr(a,'x')
# setattr(a,'x',b+1)
# print(a.x)


#(18)
# def dostuff(param1, **param2):
#     print(type(param2))
#     print(param1)
#     print(param2)
#
#
# dostuff('capitals', Arizona='Phoenix', California='Sacramento', Texas='Austin')


# (17)
# def dostuff(param1, *param2):
#     print(type(param2))
#
#
# dostuff('apples', 'bananas', 'cherry', 'dates')

# (16)
# def print_header(str):
#     print(f"+++ {str} +++")
#
#
# print_header.category = 1
# print_header.text = "some info"
#
# print_header(f" {print_header.category} and {print_header.text}")

# (15)
# def additem(listparam):
#     listparam += [1]
#
# mylist = [1,2,3,4]
# additem(mylist)
# print(len(mylist))


# (14)
# names1 = ['Amir','Barry','Chales','Dao']
#
# loc = names1.index("Edward")
#
# print(loc)


# (13)
# confusion = {}
# confusion[1] = 1
# confusion['1'] = 2
# confusion[1.0] = 4
#
# sum=0
# for k in confusion:
#     sum += confusion[k]
#
# print(f'total={sum}')

# (12)
# import re
# sum = 0
#
# pattern = 'back'
#
# if re.match(pattern,'backup.txt'):
#     sum += 1
# if re.match(pattern,'text.back'):
#     sum += 2
# if re.search(pattern,'backup.txt'):
#     sum += 4
# if re.search(pattern,'text.back'):
#     sum += 8
#
# print(sum)


# (11)
# class Person:
#     def __init__(self,id):
#         self.id = id
#
# obama = Person(100)
#
# obama.__dict__['age'] = 49
#
# print(obama.age + len(obama.__dict__))


# (10)
# values = [2,3,2,4]
#
# def my_transformation(num):
#     return num ** 2
#
# for i in map(my_transformation,values):
#     print(i)

# (9)
# for i in range(2):
#     print(i)
#
# for i in range(4,6):
#     print(i)


# (8)
# values = [1, 2, 1, 3]
# nums = set(values)
#
#
# def checkit(num):
#     if num in nums:
#         return True
#     else:
#         return False
#
#
# for i in filter(checkit, values):
#     print(i)

# (7)
# class Account:
#     def __init__(self,id):
#         self.id = id
#         id = 666
#
# acc = Account(123)
# print(acc.id)


# (6)
# class Parent:
#     def __init__(self, param):
#         self.v1 = param
#
#
# class Child(Parent):
#     def __init__(self, param):
#         self.v2 = param
#
#
# obj = Child(11)
# print(obj.v1 + " " + obj.v2)

# (5)
# print("\x48\x49!")


# (4)
# x = True
# y = False
# z = False
#
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)


# (2)
# print(type(1J))


# (3)
# d = lambda p : p * 2
# print(d)
# t = lambda p : p * 3
# print(t)
# x = 2
# print(x)
# x = d(x)
# print(x)
# x = t(x)
# print(x)
# x = d(x)
# print(x)
