class Calculate:
    def add(self, x,y):
        return x+y
    def sub(self, a, b):
        return a-b
    def div(self, a,b):
        if b == 0:
            raise ValueError("Can not divided by 0")
        return a/b