'''可以用sub匹配并替换相应字符串'''

import re
names_regex = re.compile(r'Agent \w+')
names_sub = names_regex.sub('Censoted','Agent Alice gave the secret documents to Agent bob.')
print(names_sub)

#输出结果为Censoted gave the secret documents to Censoted.
