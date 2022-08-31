"""
WARNING ... SPOILER ... 
"""

import random
random.seed()

print("1st version")

def mergesort(xs):
    n = len(xs)
    if n <= 1:
        print("base ... ", xs)
        return xs
    else:
        mid = n // 2
        left = xs[:mid]
        right = xs[mid:]
        print("xs:", xs)
        print("split")
        print("left:", left)
        print("right:", right)
        left = mergesort(left)
        right = mergesort(right)
        print("after recursion")
        print("left:", left)
        print("right:", right)
        ret = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            print("i,j:", i,j)
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
            print("ret:", ret)
        while i < len(left):
            ret.append(left[i])
            i += 1
        while j < len(right):
            ret.append(right[j])
            j += 1
        return ret

xs = list(range(10))
print(xs)
random.shuffle(xs)
print(xs)
xs = mergesort(xs)
print(xs)


print("2nd version")

def mergesort(xs):
    n = len(xs)
    if n <= 1:
        return xs
    else:
        mid = n // 2
        left = xs[:mid]
        right = xs[mid:]
        left = mergesort(left)
        right = mergesort(right)
        ret = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                ret.append(left.pop(0))
            else:
                ret.append(right.pop(0))
        if len(left) > 0:
            ret += left
        if len(right) > 0:
            ret += right
        return ret

xs = list(range(10))
random.shuffle(xs)
print(xs)
xs = mergesort(xs)
print(xs)
