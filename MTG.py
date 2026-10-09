import Cardstats

cnum = int(input("Enter a card number: "))
cname = Cardstats.getcname(cnum)
print(cname)
print(Cardstats.getcpower(cname))
print(Cardstats.getcdefence(cname))
ctype = Cardstats.getctype(cname)
print(ctype)

cccost = str(Cardstats.getc20mcost(cname))
print("Cost: " + cccost, ctype + " mana, and " + "X" + " other mana.")