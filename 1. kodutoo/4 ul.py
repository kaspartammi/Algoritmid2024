# Looge (vabalt valitud) binaarne otsingualgoritm, mis leiab kindla täisarvu
# sorteeritud täisarvude loendist.


#Funktsioon saab sisendiks sorteeritud loendi täisarvudest, arvu mida otsib ja järjekorra numbri mida tagastada(mis on alul 0).
def otsi(arr, n, i):
#  Tühi järjend uue hoidmiseks
    n_arr = []
#  Kesmise koha leidmine
    arr_k = len(arr)//2
#  Kui järjendi pikkus on 1 või alla, ja arvu ei leidu, siis tagastab vastava teksti   
    if (len(arr) <= 1) and  (arr[arr_k]!=n):
        print("täisarvu loendis pole")

# Poolitab esimes poole ja kutsub sellele rekursiivselt otsimist, kui otsitav on väiksem kui keskmine arv
    elif arr[arr_k]>n:
#         print("Esimese pooles")
        n_arr = arr[0:len(arr)//2]
#         print(n_arr)
        otsi(n_arr, n, (i +0))
        
        
# Poolitab teise poole ja kutsub sellele rekursiivselt otsimist, kui otsitav on suurem kui keskmine arv
    elif arr[arr_k]<n:
#         print("Teises pooles")
        n_arr = arr[len(arr)//2:]
#         print(n_arr)
        otsi(n_arr,n, (i +len(arr)//2))
       
# Kui arv on leitud, tagastatakse indeks    
    elif (arr[arr_k]==n):
        i +=len(arr)//2
        print(i)



arr =  [10,11,12,13,14,15]
n = 10                
otsi(arr,n,0)

