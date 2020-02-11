import re
phnum = re.compile(r'(\d{3})?(-)?(\d{4,8})')
m = phnum.search('my number is 010-2113211')
print(m.group())

