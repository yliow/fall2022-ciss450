print(42)

def f(x):
    if isinstance(x, int):
        return x * x
    elif isinstance(x, float):
        return 3.14 * x
    else:
        return None
    
def f(x):
    if isinstance(x, int):
        return x * x
    elif isinstance(x, float):
        return 3.14 * x
    else:
        raise ValueError

try:
    print(f(4))
    print(f(0.1))
    print(f("hi"))
except ValueError as e:
    print("a valueerror exception was thrown")
    print(e)
    print(type(e))

x = "abcde"
print(type(x), x)
y = [5,4,3,2,1]
print(type(y), y)
print(x[1])
print(y[1])

#     
#x = " a b c d e "
#     0 1 2 3 4 5
print(x[1:3])
print(y[1:3])
print(x[1:])
print(x[:3])
print(x[:3:2])
print(x[::2])
print(x[::-1])


x = [5,3,1,2,4]
x.sort()
print(x)

x = [5,3,1,2,4,2,2,2,2,2]
print(x.count(2))

for i in [0,1,2,3,4,5]:
    print(i)

for i in range(5, 10, 2):
    print(i)

print(range(5, 10, 2))
print(list(range(5, 10, 2)))

print('a')

