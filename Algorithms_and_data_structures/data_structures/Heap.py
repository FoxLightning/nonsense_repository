class Heap:

    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        """
        O(log(n)) enter value into heap
        """
        self.values.append(x)
        self.size += 1
        self.shift_up(self.size-1)

    def shift_up(self, i):
        """
        O(log(n))
        """
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def extract_min(self):
        """
        extract min value
        O(log(n)) depend on shift_up because heat must be move
        """
        if self.size == 0:
            return None
        if self.size == 1:
            self.values -= 1
            return self.values.pop()
        tmp = self.values[0]
        self.size -= 1
        self.values[0] = self.values[-1]
        self.values.pop()
        self.shift_down(0)
        return tmp

    def shift_down(self, i):
        """
        O(log(n))
        """

        while 2 * i + 1 < self.size:
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j:
                break
            else:
                self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j

    def show(self):
        print(self.values, self.size)

a = Heap()
n= 26
m = [5,1,7,2,7,8,5,3,1,4,7,3,1,3,6,8,34,2,1,36,2,7,3,2,2]
for i in m:
    a.insert(int(i))

a.show()

for i in range(len(m)):
    print(a.extract_min(), end=" ")