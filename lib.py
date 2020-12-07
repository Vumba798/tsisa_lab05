import matplotlib.pyplot as plt
import numpy as np
from random import uniform


tau = 1.618034
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
        self.experiments = list()
        for i in range(self.N):
            tmpX = ((self.b-self.a)
                 / (self.N+1)*(i+1) + self.a)
            tmpY = tmpX*self.c+self.d+uniform(-0.5,0.5)
            self.experiments.append(Point(tmpX, tmpY))
    def f(self, c, d, x):
        return c*x + d
    def print_experiments(self):
        for elem in self.experiments:
            elem.print()
    def sum_of_squares(self, c, d):
        sum = 0
        for point in self.experiments:
            sum += self.f(c, d, point.x) - point.y
        return sum*sum
    '''
    def _passive_search(self,epsilon, c_min, c_max,):
        res = 0.0
        n = 2
        while ((c_max - c_min) / n > eps):
            arr = []
            tmp = c_min
            step = (self.b - self.a) / n
            while tmp < d_max:
                d.append(tmp)
                tmp += step
            squares = [self._sum_of_squares(c, 0) for c in arr]
            res = d[squares.index(min(squares))]
            n += 1
        return res
        '''
    def passive_search(self, epsilon, c_min, c_max, d_min, d_max):
        N = 0
        while (c_max - c_min) / (N + 1) > epsilon:
            N += 1
        '''
        optimum_c = 1/(N+1)*(c_max - c_min) + c_min
        opt_sum = self.sum_of_squares(optimum_c, 0)
        for i in range(N):
            current_c = i/(N+1)*(c_max-c_min) + c_min
            print("current c =", current_c)
            current_sum = self.sum_of_squares(current_c, 0)
            print("current_sum =", current_sum)
            if current_sum < opt_sum:
                optimum_c = current_c
                opt_sum = current_sum
            print("optimum_sum =", opt_sum)
        '''
        c_arr = []
        for i in range(N):
            c_arr.append(i/(N+1)*(c_max-c_min) + c_min)
        squares = []
        for c_tmp in c_arr:
            d = self.golden_section(epsilon, d_min, d_max, c_tmp)
            squares.append(self.sum_of_squares(c_tmp, d))
        for elem in squares:
            print("square =", elem)
        self.c_ = c_arr[squares.index(min(squares))]
        self.d_ = self.golden_section(epsilon, d_min, d_max, self.c_)
    def golden_section(self, epsilon,
                        d_min, d_max, c):
        left = d_min
        right = d_max
        while right - left > epsilon:
            print("left =", left)
            print("right =", right)
            d_right = (right - left) / tau + left;
            d_left = right - (right - left) / tau
            print(self.sum_of_squares(c, d_left))
            print(self.sum_of_squares(c, d_right))
            if abs(self.sum_of_squares(c, d_left)) < abs(self.sum_of_squares(c, d_right)):
                right = d_right
            else:
                left = d_left
        return (left + right) / 2
    def print(self):
        print("C = ", self.c_)
        print("D = ", self.d_)
    def draw(self):
        x_arr = []
        y_arr = []
        x = np.linspace(self.a, self.b)
        y = self.c_ * x + self.d_
        for point in self.experiments:
            x_arr.append(point.x)
            y_arr.append(point.y)
        plt.scatter(x_arr, y_arr)
        plt.plot(x, y)
        plt.show()
nn = NeuralNetwork(3, 1, -2, 2, 16)
nn.print_experiments()
nn.passive_search(0.1, 0.1, 10, -4, 4)
nn.golden_section(0.1, -4, 4, nn.c_)
nn.print()
nn.draw()
'''
import numpy as np
def f(x):
    return (x - 1)*(x-1)

N = 0
eps = 0.1
x_min = -2
x_max = 2
while (x_max - x_min) / (N + 1) > eps:
    N += 1
print(N)
x_arr = []
min_el = x_max
for i in range(N):
    x_arr.append(i/(N+1)*(x_max - x_min) + x_min)
    if f(x_arr[len(x_arr) - 1]) < f(min_el):
        min_el = x_arr[len(x_arr) - 1]
print(min_el)
'''
