import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

'''根据数据绘制引力波'''
rate_h, hstrain = wavfile.read(r'data/ylb/H1_Strain.wav','rb')#利用wavfile将wav文件转化为数据。
rate_l, lstrain = wavfile.read(r'data/ylb/L1_Strain.wav','rb')
reftime, ref_H1 = np.genfromtxt('data/ylb/wf_template.txt').transpose()

htime_interval= 1/rate_h#用频率求出时间
ltime_interval= 1/rate_l

htime_len =hstrain.shape[0]/rate_h
htime = np.arange(-htime_len/2,htime_len/2,htime_interval)#计算出横轴时间坐标
ltime_len =lstrain.shape[0]/rate_l
ltime = np.arange(-ltime_len/2,ltime_len/2,ltime_interval)

fig= plt.figure(figsize=(12,6))

plth = fig.add_subplot(221)#在2行2列的第一幅
plth.plot(htime,hstrain,'y')
plth.set_xlabel('Time(seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

pltl = fig.add_subplot(222)#在2行2列的第二幅
pltl.plot(ltime,lstrain,'g')
pltl.set_xlabel('Time(seconds)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')

pltref = fig.add_subplot(212)在2行1列的第2幅
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time(seconds)')
pltref.set_ylabel('Template Strain')
pltref.set_title('Template')
fig.tight_layout()

plt.savefig('data/ylb/Gravitational_Wave_Original.png')#存储
plt.show()#展示
plt.close(fig)
