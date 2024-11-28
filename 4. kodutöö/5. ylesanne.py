class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.DELETED = "DELETED"  # Märk kustutatud elemendi kohta

    def hash1(self, key):
#Esimene räsifunktsioon.
        return key % self.size

    def hash2(self, key):
#Teine räsifunktsioon 
        return 1 + (key % (self.size - 1))

    def insert(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        for _ in range(self.size):
            if self.table[index] is None or self.table[index] == self.DELETED:
                self.table[index] = key
                return
            index = (index + step) % self.size

        raise Exception("Hash table is full")

    def search(self, key):
        index = self.hash1(key)
        step = self.hash2(key)

        for _ in range(self.size):
            if self.table[index] is None:
                return False  # Võtit ei leitud
            if self.table[index] == key:
                return True  # Võti leiti
            index = (index + step) % self.size

        return False  # Võtit ei leitud pärast kogu tabeli läbimist

    def delete(self, key):
        index = self.hash1(key)
        step = self.hash2(key)

        for _ in range(self.size):
            if self.table[index] is None:
                return False  # Võtit ei leitud
            if self.table[index] == key:
                self.table[index] = self.DELETED
                return True  # Võti kustutati
            index = (index + step) % self.size

        return False  # Võtit ei leitud

    def display(self):
        print("Hash Table:")
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")


# Driver kood
if __name__ == "__main__":
    size = 7
    keys = [50, 700, 76, 85, 92, 73, 101]

    hash_table = DoubleHashingHashTable(size)

    for key in keys:
        try:
            hash_table.insert(key)
        except Exception as e:
            print(e)

    hash_table.display()
    print("Otsime 73:", hash_table.search(73))
    print("Kustutame 76:", hash_table.delete(76))
    hash_table.display()
