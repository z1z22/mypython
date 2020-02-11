def is_palindrome(n):
	'''打印回数,即正反看都一样的数'''
	return str(n) == str(n)[::-1]#[::-1]可以将字符串反相排列

k = filter(is_palindrome,range(10,100000))
print(list(k))


b = reversed('refda')
print(lisr(b))
