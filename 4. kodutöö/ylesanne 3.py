class Node:
#     Ühendatud nimekirja sõlm.
    def __init__(self, key):
        self.key = key
        self.next = None


class Hash:
#     Hash tabel, 
    def __init__(self, bucket):
        self.__bucket = bucket
        self.__table = [None for _ in range(bucket)]  # Algul kõik pesad on tühjad

    def hashFunction(self, key):
        return key % self.__bucket

    def insertItem(self, key):
        index = self.hashFunction(key)
        new_node = Node(key)
        # Lisa uus sõlm seotud nimekirja algusesse
        if self.__table[index] is None:
            self.__table[index] = new_node
        else:
            # Lisa sõlm olemasoleva nimekirja algusesse
            new_node.next = self.__table[index]
            self.__table[index] = new_node

    def deleteItem(self, key):
        index = self.hashFunction(key)
        current = self.__table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.__table[index] = current.next
                return
            prev = current
            current = current.next

    def displayHash(self):
        for i in range(self.__bucket):
            print(f"[{i}]", end="")
            current = self.__table[i]
            while current:
                print(f" --> {current.key}", end="")
                current = current.next
            print()


# Näide kasutamisest
if __name__ == "__main__":
    pikkus = 7
    a = [15, 11, 27, 8, 12]

    h = Hash(pikkus)

    # Sisesta võtmed hash-tabelisse
    for x in a:
        h.insertItem(x)

    # Kustuta üks võti
    h.deleteItem(12)

    # Kuvame hash-tabeli
    h.displayHash()
