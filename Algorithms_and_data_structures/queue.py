class queue:
    a = []
    def __init__(self,*m):
        self.a += m
    def add(self, *m):
        self.a += m
    def popleft(self):
        t = (self.a)[0]
        self.a = (self.a)[1:]
        return t




if __name__ == "__main__":
    """
    run test if file running as a main program
    """
    import doctest
    doctest.testmod()





