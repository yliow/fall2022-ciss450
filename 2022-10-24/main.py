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
    for key in csp.C:
        c = csp.C[key]
        print(key, c)
        for var,val in assignments:
            print(var, '->', val)
            if isinstance(val, str):
                c = c.replace(var, "'%s'" % val)
        print(c)
        print(eval(c))

print("Testing check_constraints ...")
assignments0 = [('V1', 'R'), ('V2', 'G')]
check_constraints(csp, assignments0)


#assignments1 = [('V1', 'R'), ('V2', 'R')]
