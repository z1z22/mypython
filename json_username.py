import json
while True:
    username = input('Please input your name(q to quit): ')
    if username == "q":
        break
    else:
        filename = "usernames.json"
        with open(filename, 'a') as f_obj:
            username_full = '\nUsername:   ' + username
            json.dump(username_full, f_obj)
            print('We will remamber your name:  ', username)