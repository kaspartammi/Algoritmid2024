
#järjekorda lisamine, sisendiks järjekord ja elemendid mis sellese lisada
def lisa(järjekord, lisa):
     
    for i in range(len(lisa)):
        järjekord.append(lisa[i])      
    return järjekord
    
#järjekorda lisamine, sisendiks järjekord ja number, mitu elementi sellest eemaldada. Prindib välja iga elemendi, mis eemaldatakse järjekorrast.
def eemalda(järjekord, n):
    if n <= len(järjekord):        
        for i in range(n):
            eemaldatud = järjekord.pop(0)
            print("Eemaldati element: ", eemaldatud)
            n -=1
    else:
        print("Soovid eemaldada rohkem elemente kui järjekorras on")
 


#Järjekorra kasutus, järjekorras on juba mõned elemendid, järjekorda lisatakse elemente ja seejärel eemaldatakse neid.
järjekord = [1,2]
juurde = [5,6,7]
lisa(järjekord, juurde)
eemalda(järjekord, 3)


# Ajaline keerukus:
# Järjekorra välja kutsumine = 1
# Lisamine pole konstantne, sõltub lisatud elementide arvust = n
# Eemaldamine pole konstantne, sõltub eemaldavate elementide arvust = n
# Kokku 1 + n + n = O(n)
