filename = 'namelist.txt'
with open(filename, "a") as nl:
    while True:
        name = input("请输入你的名字(q退出):  ")
        if name == "q":
            break
        else:
            nl.write(name + " \n")