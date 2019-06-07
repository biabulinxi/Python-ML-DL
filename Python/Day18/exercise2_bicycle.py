# @Project:AID1810
# @Author:biabu
# @Date:18-11-26 下午6:22
# @File_name:exercise2_bicycle.py
# @IDE:PyCharm

class Bicycle:
    def run(self, km):
        print("自行车骑行了%d公里" % km)

class EBicycle(Bicycle):
    def __init__(self,volume):
        self.volume = volume
        print('新买的电动车内有%d度电' % volume)

    def run(self,km):
        sub_km = km - self.volume * 10
        if sub_km < 0:
            self.volume -= km // 10
            print('电动骑行了%dkm, 还剩%d度电' % (km,self.volume))
        else:
            self.volume = 0
            print('电动骑行了%dkm, 还剩%d度电,' % (km - sub_km,
                                         self.volume),end='')
            super().run(sub_km)

    def fill_charge(self,vol):
        self.volume += vol
        print('电动自行车充电%d度' % vol)

b = EBicycle(5) #新买的电动车内有5度电
b.run(10) #电动骑行了10km里, 还剩4度电
b.run(100) #电动骑行了40km里, 还剩0度电, 自行车骑行了60km
b.fill_charge(10) #电动自行车充电10度
b.run(50)   #电动骑行了50km里, 还剩5度电
