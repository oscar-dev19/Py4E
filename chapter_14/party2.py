class PartyAnimal:
    x = 0
    name =''
    def __init__(self,nam):
        self.name = nam
        print("{nam} is constructed".format(nam=self.name))

    
    def party(self):
        self.x +=1
        print("so far:",self.x)


    def __del__(self):
        print("I am destructed",self.x)


an = PartyAnimal('Ann')

for _ in range(4):
    an.party()

PartyAnimal.party(an)
an = 42
print("an contains:",an)
