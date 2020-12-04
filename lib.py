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
    tau = 1.618034
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
    def f(self,  float: x):
        return c*x + d
    def print_experiments(self):
        for elem in self.xArr:
            elem.print()
    def sum_of_squares(self, float: c, float: d):
        sum = 0
        for i in range(self.N):
            sum += f(xArr[i])
        return sum
    def create_coef_list(self, float: epsilon,
                        float: c_min, float: c_max):
        left = c_min
        right = c_max
        while right - left > epsilon:
            c_right = (right - left) / tau + left;
            c_left = (rihgt - left) / tau - right
            if sum_of_squares(c_left) < c_right):
                right = c_right
            else:
                left = c_left

             

nn = NeuralNetwork(3, 1, -2, 2, 3)
nn.print_experiments()

