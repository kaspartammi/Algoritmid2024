def fibo(n):
# kui sisend on 1 või väiksem, tagastab 1, sest olem jõudnud algusesse 
    if n <= 1:
        return n
# Fibonacci number moodustub 2 eelneva Fibonacci numbri summast. Seega võtame otsitud arvule eelnevad fibonacci arvud, ja kutsume funktsiooni nende arvudega välja.
# Lõpptulemuse saamiseks liidetakse kõik returnitud arvud kokku ja saadakse n-is fibonacci arv
    return fibo(n-1) + fibo(n-2)
    
    


print(fibo(9))
