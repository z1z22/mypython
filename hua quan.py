import random
'随机数划拳'

p = int(input('请随机输入你出的剪刀(1)、石头(2)、布(3):'))
i = random.randint(1,3)	

print('你出的是%d,对方出的是%d' %(p,i))

if p == i:
   	print('平手,再来')
elif p > 3:
	print('你的出拳不合法')
elif ((p == 1 and i == 3) 
		or (p == 2 and i == 1) 
		or (p ==3 and i == 2)):
   	print('恭喜,你赢了')
else:
	print('你输了,笨死算了')


