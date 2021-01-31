from party2 import PartyAnimal

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

for _ in range(4):
    s.party()
    j.party()

s.party()
j.party()
