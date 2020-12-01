class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        m = []
        cur = self.head
        while cur is not None:
            m.append(cur[0])
            cur = cur[1]
        return str(m)


    def add(self, element):
        if not self.search(element):
            node = [element, None]

            if self.head is None:
                self.head = node
            else:
                self.tail[1] = node

            self.tail = node

    def search(self, element):
        curr = self.head
        deep = 1
        while curr is not None:
            if curr[0] == element:
                return deep
            curr = curr[1]
            deep += 1
        return False

class HashTable:
    def __init__(self):
        self.table = [LinkedList() for i in range(32)]
    def __str__(self):
        m = []
        for i in self.table:
            m.append(str(i))
        return str(m)


    def add(self, element):
        def calc_hash(data):
            k = 3571
            s = 0
            i = 1
            data += 8432941
            while data > 0:
                s += data % 2 * k ** i
                i += 1
                data //= 2
            return s % 32
        hsh = calc_hash(element)
        self.table[hsh].add(element)
    def search(self, element):
        def calc_hash(data):
            k = 3571
            s = 0
            i = 1
            data += 8432941
            while data > 0:
                s += data % 2 * k ** i
                i += 1
                data //= 2
            return s % 32
        hsh = calc_hash(element)
        return [hsh, self.table[hsh].search(element)]

    

a = HashTable()

for i in range(123):
    a.add(i)

print(a.search(5))

    
print(a)



    