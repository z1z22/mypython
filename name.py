def greet_users(names):
    '''names作为列表,问候列表中的人'''
    for name in list(names):
        msg = 'hello, ' + name.title() + '!'
        
        print(msg)
    
usernames = ['fdafd', 'fdasfd', 'ghjgj']
print(greet_users(usernames))


