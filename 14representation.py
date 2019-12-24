# special methods
# 1.__bool__
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
jc = Account('Jack')
bool(jc)  # True. by default
Account.__bool__ = lambda self: self.balance != 0
bool(jc) #False. if an object define the __bool__ method, then python call that method to determine True or False

# 2.__call__ define object that can be called
class adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, k):
        return self.n + k
add_three = adder(3)
add_three(4) #7


# multiple representation
# highest abstraction
class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)

class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)

from math import atan2
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)
from math import sin, cos, pi
class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)
