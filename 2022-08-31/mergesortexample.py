import random
random.seed()

def mergesort(xs):
    n = len(xs)
    if n <= 1:
        return xs
    else:
        mid = n // 2
        left = xs[:mid]
        right = xs[mid:]
        #print(xs)
        #print(left)
        #print(right)
        left = mergesort(left)
        right = mergesort(right)
        ret = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
        return ret

xs = list(range(10))
print(xs)
random.shuffle(xs)
print(xs)
mergesort(xs)
