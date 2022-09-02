class vec2d:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "<%s, %s>" % (self.__x, self.__y)

    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
    x = property(get_x, set_x)

    def get_y(self):
        return self.__y
    def set_y(self, y):
        self.__y = y
    y = property(get_y, set_y)

    def __add__(self, v):
        ret = vec2d(self.__x + v.__x, self.__y + v.__y)
        return ret

    def __len__(self):
        return 2

    # += is __iadd__
    
v = vec2d(1, 2)
print(v)
v.x = 42
print(v.x)
u = vec2d(7, 1)
print("u:", u)
w = v + u
print("w:", w)
print("len(w):", len(w))


class P:
    def __init__(self, x):
        self.x = x

class C(P):
    def __init__(self, x, y):
        P.__init__(self, x)
        self.y = y
        
