"""            example of coloring      NOT coloring
v1 -- v2       v1=RED   v2=GREEN        v1=RED   v2=GREEN
| \   |
|  \  |
|   \ |
v3 -- v4       v3=GREEN v4=BLUE         v3=BLUE  v4=BLUE
"""
class CSP:

    def __init__(self, V, D, C):
        self.V = V
        self.D = D
        self.C = C

csp = CSP(V = ['V1', 'V2', 'V3', 'V4'],
          D = {'V1':['R', 'G', 'B'],
               'V2':['R', 'G', 'B'],
               'V3':['R', 'G', 'B'],
               'V4':['R', 'G', 'B']},
          C = {('V1', 'V2'): 'V1 != V2',
               ('V1', 'V3'): 'V1 != V3',
               ('V1', 'V4'): 'V1 != V4',
               ('V2', 'V4'): 'V2 != V4',
               ('V3', 'V4'): 'V3 != V4',               
              },
)        
'''
vars = v1,v2,v3,v4
assignments = [('V1', 'R'), ('V2', 'G')]
goal_test is length of assignments == 4 and all assignments are "consistent
eval("V1 != V2" ...substitute "V1" with "R", "V2" with "G") -> True
'''

def check_constraints(csp, assignments): # is_consistent
    """
    Return True if assignments are consistent, i.e., no constriant in csp is violated
    """
    da = dict(assignments)
    da_keys = set(da.keys())
    for key in csp.C:
        c = csp.C[key]
        c_keys = set(key)
        print("da_keys:", da_keys)
        print("c_keys:", c_keys)
        # c can be evaluated if c_keys is a subset of da_keys
        if c_keys.issubset(da_keys):
            print(key, c)
            for var,val in assignments:
                print(var, '->', val)
                if isinstance(val, str):
                    c = c.replace(var, "'%s'" % val)
                elif isinstance(val, (int, float, bool)):
                    c = c.replace(var, "%s" % val)
                else:
                    raise ValueError("ERROR: %s of type %s is not supported" % (val, type(val)))
            print(c)
            print(eval(c))

print("Testing check_constraints ...")
assignments0 = [('V1', 'R'), ('V2', 'G')]
check_constraints(csp, assignments0)


#assignments1 = [('V1', 'R'), ('V2', 'R')]
