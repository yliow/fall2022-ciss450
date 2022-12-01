import math

def S(z):
    return 1.0 / (1.0 + math.exp(-z))

def f(z):
    if z <= 0.5:
        return 0.0
    else:
        return 1.0

def A(z):
    return f(S(z))

class Neuron:
    def __init__(self, ws, A):
        self.ws = ws
        self.A = A
    def __call__(self, *args):
        #print("args:", args)
        #print("args[0]:", args[0])
        #print("args[1]:", args[1])
        s = 0.0
        args = [1.0] + list(args)
        for w, x in zip(self.ws, args):
            s += w * x
        return self.A(s)


AND = Neuron([0.9, 0.1, 0.1], A)
print(AND(1, 1))
print(AND(1, 0))
print(AND(0, 1))
print(AND(0, 0))
