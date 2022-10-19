for i in range(2):
    for j in range(2):
        exec("X%s%s = 1" % (i,j))

# also test out eval("1 + 2")
print(X01)

# model = assignment of value to variables
# say variables are X, Y, Z
# dict
# list
model = {'X': 1,
         'Y': 2,
         'Z': None}

# V00, V01, ..., V88
print("creating 99 vars, all with domain [0,1,2,3]")
vars = []
doms = {}
for r in range(9):
    for c in range(9):
        vars.append("V%s%s" % (r, c))
print(vars)
for var in vars:
    doms[var] = [0,1,2,3]
print(doms)
