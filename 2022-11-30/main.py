import math
import numpy as np
import itertools

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


class NeuralLayer:
    def __init__(self, neurons):
        self.neurons = neurons
    def __call__(self, *args):
        return [n(*args) for n in self.neurons]


class ANN:
    def __init__(self, layers):
        self.layers = layers
    def __call__(self, *args):
        for layer in self.layers:
            args = layer(*args)
        return args

    
def find_neuron(tests, M=1, step=0.1, verbose=False, errorbound=0.0):
    """
    If M = 5, step = 0.001, tests weights in [-5, 5] by step of 0.001
    """
    n = len(tests[0][0])                                        # number of non-bias weights
    interval = np.arange(-M, M + step, step)                    # weights for one input
    cube = itertools.product(*[interval for _ in range(n + 1)]) # (n + 1)-dim cube of all weights
    for w in cube:
        if verbose: print("testing weights", w)
        n = Neuron(w, A)
        found = True
        for x, expected in tests:
            if verbose: print("  testing test case:", x, expected)
            if abs(n(*x) - expected) > errorbound:
                found = False
                break
        if found:
            return w

tests = [((1, 1), 1),
         ((1, 0), 0),
         ((0, 1), 0),
         ((0, 0), 0)]
ret = find_neuron(tests)
if ret != None:
    w0, w1, w2 = ret
    print("found AND model:", w0, w1, w2)                
    AND = Neuron([w0, w1, w2], A)
else:
    print("ERROR: cannot find AND model")
    AND = None

tests = [((1, 1), 1),
         ((1, 0), 1),
         ((0, 1), 1),
         ((0, 0), 0)]
ret = find_neuron(tests)
if ret != None:
    w0, w1, w2 = ret
    print("found OR model:", w0, w1, w2)                
    OR = Neuron([w0, w1, w2], A)
else:
    print("ERROR: cannot find AND model")
    OR = None

tests = [((1,), 0),
         ((0,), 1)]
ret = find_neuron(tests)
if ret != None:
    w0, w1 = ret
    print("found NOT model:", w0, w1)                
    NOT = Neuron([w0, w1], A)
else:
    print("ERROR: cannot find NOT model")
    NOT = None


print("computing XOR model")
ret = find_neuron([((0,0),0),
                   ((0,1),1),
                   ((1,0),1),
                   ((1,1),0),
])
print(ret)
#print(w0, w1, w2)
#OR = Neuron

#==============================================================================
# ANN for XOR
#==============================================================================

# Find (x,y) -> x * y'
tests = [((1, 1), 0),
         ((1, 0), 0),
         ((0, 1), 1),
         ((0, 0), 0),
         ]
ret = find_neuron(tests)
if ret != None:
    w0, w1, w2 = ret
    print("found NOT_AND model:", w0, w1, w2)                
    NOT_AND = Neuron([w0, w1, w2], A)
else:
    print("ERROR: cannot find NOT_AND model")
    NOT_AND = None

# Find (x,y) -> x * y'
tests = [((1, 1), 0),
         ((1, 0), 1),
         ((0, 1), 0),
         ((0, 0), 0),
         ]
ret = find_neuron(tests)
if ret != None:
    w0, w1, w2 = ret
    print("found AND_NOT model:", w0, w1, w2)                
    AND_NOT = Neuron([w0, w1, w2], A)
else:
    print("ERROR: cannot find AND_NOT model")
    AND_NOT = None

layer0 = NeuralLayer([AND_NOT, NOT_AND])
layer1 = NeuralLayer([OR])
XOR = ANN([layer0, layer1])
print("XOR:")
print(XOR(1, 1))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(0, 0))
