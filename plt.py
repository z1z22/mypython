import matplotlib.pyplot as plt
squares = [i * i for i in range(10)]
plt.plot(squares,linewidth=5)

plt.title('squares numbers', fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('square of value',fontsize=14)

plt.tick_params(axis='both', labelsize=14)#设置刻度标记大小
plt.show()