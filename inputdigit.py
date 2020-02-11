def inputdigit(input_str):
    '''输入数字'''
    while True:
        i_str = input(input_str)

        if i_str.isdigit():
            return int(i_str)
            break
        elif i_str == 'q' or i_str == 'Q':
            exit()
        else:
            print("Please input digit('Q'uit).")