def is_palindrome(n):
	return str(n) == str(n)[::-1]

k = filter(is_palindrome,range(10,100000))
print(list(k))
