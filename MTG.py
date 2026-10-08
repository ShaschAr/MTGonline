import Cardstats

cnum = int(input("Enter a card number: "))
cname = Cardstats.test(cnum)
print(cname)
print(Cardstats.getcpower(cname))
print(Cardstats.getcdefence(cname))
print(Cardstats.getctype(cname))