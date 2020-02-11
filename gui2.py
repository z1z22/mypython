import tkinter as tk

class APP(object):
    """docstring for APP"""
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side = tk.LEFT,padx=100,pady = 100)#调整窗口
        self.hi_there  = tk.Button(frame, text = '打招呼',fg= 'blue',  command = self.say_hi)
        self.hi_there.pack()
    def say_hi(self):
        print('各位大家好，这个是图形界面')



root= tk.Tk()
app = APP(root)
root.mainloop()
