import tkinter as tk
#实例化
app = tk.Tk()
# 设置title
app.title('zhouzhu')

thelabel = tk.Label(app, text = '显示出来看看')
thelabel.pack()
#运行显示
app.mainloop()
