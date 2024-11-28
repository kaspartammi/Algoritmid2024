#Index Mapping

andmed = [1, 2, 3, 4, 6, 7, 8]

def indexMapping(andmed):
    
    suurus = max(andmed)
    
    massiiv = [0] *(suurus+1)
    
    for väärtus in andmed:
        massiiv[väärtus] = 1
        
    return massiiv


def otsi(massiiv, väärtus):
    if massiiv[väärtus] == 1:
        print("Väärtus ",väärtus," on olemas.")
    elif massiiv[väärtus] == 0:
         print("Väärtus ", väärtus, " puudub.")
    

andmed = [1, 2, 3, 4, 6, 7, 8]
massiiv = indexMapping(andmed)
otsi(massiiv,1)
otsi(massiiv, 5)