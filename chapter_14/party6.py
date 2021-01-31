from party2 import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points +=6
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal('Sally')
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print('dir',dir(j))
