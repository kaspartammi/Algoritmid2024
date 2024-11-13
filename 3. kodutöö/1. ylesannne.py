#  Lineaarotsing

def lineaarotsing(loend, otsitav):
    for i in loend:
        if i == otsitav:
            print("otsitud element ", otsitav, " asub loendis kohal ", (loend.index(i)+1))


a = [100, 200, 300]
b = 200

lineaarotsing(a, b)