from random import uniform
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print(self):
        print("X =", self.x)
        print("Y =", self.y)
        print()
class NeuralNetwork:
    def __init__(self, c, d, a, b, N):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.N = N
        self.xArr = list()

        for i in range(self.N):
            tmpX = ((self.b-self.a)
                 / (self.N+1)*(i+1) + self.a)
            tmpY = tmpX*self.c+self.d+uniform(-0.5,0.5)
            self.xArr.append(Point(tmpX, tmpY))
    def print_experiments(self):
        for elem in self.xArr:
            elem.print()

nn = NeuralNetwork(3, 1, -2, 2, 3)
nn.print_experiments()
