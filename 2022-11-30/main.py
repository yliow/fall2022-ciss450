import math

def S(z):
    return 1.0 / (1.0 + math.exp(-z))

def f(z): # treshold function
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


def test(testcases):
    for w0 in range(-10, 11):
        w0 = w0 / 10.0
        for w1 in range(-10, 11):
            w1 = w1 / 10.0
            for w2 in range(-10, 11):
                w2 = w2 / 10.0
                
                n = Neuron([w0, w1, w2], A)
                found = True
                for x1, x2, correct in testcases:
                    if n(x1, x2) != correct:
                        found = False
                        break
                if found:
                    return w0, w1, w2
    return None

print("computing AND model")
w0, w1, w2 = test([(0,0,0),
                   (0,1,0),
                   (1,0,0),
                   (1,1,1),
    ])
print(w0, w1, w2)
AND = Neuron([w0, w1, w2], A)

print("computing OR model")
w0, w1, w2 = test([(0,0,0),
                   (0,1,1),
                   (1,0,1),
                   (1,1,1),
    ])
print(w0, w1, w2)
OR = Neuron([w0, w1, w2], A)


print("computing XOR model")
ret = test([(0,0,0),
            (0,1,1),
            (1,0,1),
            (1,1,0),
    ])
print(ret)
#print(w0, w1, w2)
#OR = Neuron
