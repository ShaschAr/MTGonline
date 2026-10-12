import Cardstats
cnum = 0

while cnum != "stop":
    cnum = int(input("Enter a card number: "))
    cname = Cardstats.getcname(cnum)
    print(cname)

    cuse = Cardstats.getcuse(cname)
    csubtype = Cardstats.getcsubtype(cname)
    if cuse == "Artifact" and not csubtype == "Creature":
        print(csubtype, cuse)
    elif csubtype == "N/A":
        print(cuse)
    else: 
        print(cuse, csubtype)
    
    print(Cardstats.getcpower(cname))
    print(Cardstats.getcdefence(cname))
    ctype = Cardstats.getctype(cname)
    print(ctype) 

    cmcost = str(Cardstats.getcmcost(cname))
    omcost = str(Cardstats.getomcost(cname))
    if ctype != "Artifact" or ctype != "Land":
        print("Cost: " + cmcost, ctype + " mana, and " + omcost + " other mana.")
    elif ctype == "Artifact":
        print("Cost: " + omcost + " mana.")
    else:
        print("Free")