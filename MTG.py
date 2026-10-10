import Cardstats
cnum = 0

while cnum != "stop":
    cnum = int(input("Enter a card number: "))
    cname = Cardstats.getcname(cnum)
    print(cname)
    cuse = Cardstats.getcuse(cname)
    print(cuse)
    print(Cardstats.getcpower(cname))
    print(Cardstats.getcdefence(cname))
    ctype = Cardstats.getctype(cname)
    print(ctype)

    if ctype != "Artifact" or ctype != "Land":
        cccost = str(Cardstats.getcmcost(cname))
        print("Cost: " + cccost, ctype + " mana, and " + "X" + " other mana.")