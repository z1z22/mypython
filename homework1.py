# # def func():
# #     n = 5
# #     list1 = [1,3,5,7,8,9,]
# #     def inner_func():
# #         nonlocal n
# #         for index, x in enumerate(list1):
# #             list1[index] = x + n

# #         list1.sort()
# #         n+=1

# #     inner_func()
# #     print(list1)
# #     print(n)

# # func()


# def func(a,b):
#     c = 10
#     def inner_func():
#         s = a + b + c
#         print('结果是：' ,s)
#     return inner_func

# result1 = func(7,8)
# result1()
# result2 = func(2,3)
# result2()
# result1()
import time
import urllib.request
import urllib.parse
# islogin = False

# def login():
#     username = input('输入用户名：')
#     password = input('输入密码：')
#     if username == 'admin' and password == '123456':
#         return True
#     else:
#         return False

# def login_requited(func):
#     def wrapper(*args, **kwargs):
#         global islogin
#         print('-----------付款----------')
#         if islogin:
#             func(*args, **kwargs)
#         else:
#             print('你没有登陆')
#             islogin = login()
#             print('result', islogin)
#     return wrapper

# @login_requited
# def pay(money):
#     print('正在付款，付款金额是{}'.format(money))
#     print('付款中')
#     time.sleep(2)
#     print('付款完成')

# pay(10000)

# pay(3000)

# max()
# filter()
# sorted
