def make_pizza(size, *toppings):  #*toppings代表名为topping的一个空元组.要放在最后
    '''制作披萨'''
    print('\n制作' + str(size) + '英寸大小的披萨用下列原料:' )
    for topping in toppings:
        print('--'+topping.title())