from functools import reduce
'''求几个数的最大公因数'''
# s_list = [] #创建列表存储输入的数字
# x = 1
# while x != "q":
#     x = input('请输入数字, q开始计算:')
#     if x != 'q':
#         s_list.append(int(x))

# l_list = []#创建列表存储所有数的因数
# for i in s_list:
#     r_list = []#创建列表存储每个数的因数
#     for n in range(1, i+1):
#         if  i % n == 0:
#             r_list.append(n)
#     l_list.append(r_list)


def fenjie(i):
    r_list = []  # 创建列表存储每个数的因数
    for n in range(1, i + 1):
        if i % n == 0:
            r_list.append(n)
    return r_list


def f(x, y):
    # 创建函数求列表的交集
    return list(set(x) & set(y))


def main():
    s_list = []  # 创建列表存储输入的数字
    x = 1
    while x != "q":
        x = input('请输入数字, q开始计算:')
        if x != 'q':
            s_list.append(int(x))
    l_list = map(fenjie, s_list)
    result = reduce(f, l_list)  # 用reduce计算所有列表交集
    print('{}的公因数是{}, 最大公因数是{}'.format(s_list, result, max(result))

if __name__ == '__main__':

    main()
