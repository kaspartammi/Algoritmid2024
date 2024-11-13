# kahendotsing

def kahendotsing (järjend, otsitav, esimene, teine):
    while  esimene <= teine:
        
        keskmine = esimene +(teine-esimene)//2
        
        if järjend[keskmine] == otsitav:
            return keskmine

        elif järjend[keskmine] < otsitav:
            esimene = keskmine+1
        
        else:
            teine = keskmine - 1
    
    
    
    
    
a = [100, 200, 300, 400, 500, 600,700]
b = 600

print("Otsitav element asub järjendis järjekorras ",(kahendotsing(a, b, 0, len(a)-1)+1)," kohal")