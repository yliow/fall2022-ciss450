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

v = vec2d(1, 2)
print(v)
v.x = 42
print(v.x)
