fp = open('pengfu.txt', 'r', encoding = 'utf8' )
string = fp.read()
fp.close()
lt = eval(string)
print(lt)
print()
print(string)
print('strint type: ',type(string))
print('lt type: ',type(lt))
print(lt[0]['内容'])