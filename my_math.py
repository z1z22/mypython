import math

def quadratic(a, b, c):
    '''已知a,b,c,求二元一次方程的解'''
    if a ==0:
        x = (-c)/b
        return x
    else:
        k = b * b - 4 * a * c
        if k > 0:
            x1 = (-b + math.sqrt(k))/(2 * a)
            x2 = (-b - math.sqrt(k))/(2 * a)
            result = [x1, x2]
            return(set(result))
        else:
            return('No result')
            

def product(*number):
    '''计算任意几个数的乘积'''
    m = 1
    for n in number:
        m *= n
    return m


def collatz(number):
    '''如果参数是偶数,就除2。如果是奇数，就返回 3*number+1.最后总会等于1'''
        if number == 0:
            return 1
            print('error')
        elif number%2 == 0:
            return(number // 2)
           
        else:
            return(number * 3 +1)

i=45   #i=5反复调用此函数
while i != 1:
    i = collatz(i)
    print(i)



#生成所有的素数primes:
def _odd_iter():
    '''建一个生成器,生成3开始的奇数数列''' 
    n = 1
    while True:
        n += 2
        yield n
        
def _not_divisible(n):
    '''定义一个素数的筛选函数'''
    return lambda x: x % n > 0

def primes():
    '''定义一个生成器,不断的返回下一个素数'''
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it)#返回序列的一个数
        yield n
        it = filter(_not_divisible(n),it)
    
for n in primes():
    '''打印1000 以内的素数'''
    if n < 1000:
        print(n)
    else:
        break           
        
