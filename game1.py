class Dog():
    """docstring for Dog"""
    def __init__(self, name, blood=100, attrc=50):
        self.name = name 
        self.blood = blood
        self.attrc = attrc
    def attredf(self,persen):
        persen.blood -= self.attrc
        if persen.blood <= 0:
            print('%s挂了' %persen.name)
        else:
            pass
            print('%s被%s打了，掉了%s血,还剩%s。' %(persen.name, self.name, self.attrc, persen.blood))

class Persen():
    """docstring for Percent"""
    def __init__(self, name, blood=100, attrc=50):
        self.name = name
        self.blood = blood
        self.attrc = attrc

    def attredf(self,dog):
        dog.blood -= self.attrc
        if dog.blood <= 0:
            print('%s挂了' %dog.name)
        else:
            print('%s被%s打了，掉了%s血,还剩%s。' %(dog.name, self.name, self.attrc, dog.blood))


zhuzhu = Dog('zhuzhu')
zhourz = Persen('zhourz', 500, 100)

zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhuzhu.attredf(zhourz)
zhourz.attredf(zhuzhu)


        
        