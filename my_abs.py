def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad Type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs("s"))
