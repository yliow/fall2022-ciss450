"""
Backtracking search

Example: knight's tour problem.

General idea:
Each recursive function call is a search node.
The function runs through all the possible single-step -- one edge of the
state graph.
Then I pass this solution + one step to the next search node, i.e.,
the next recursive function call.

X = set to record what squares have been taken
X is hashtable of [(2, 3), (4, 5)], i.e., (2, 3), (4,5)
have been taken.
deque to record the path. Example deque is [(2,3),(4,5)].
This means first step is at (r,c) = (2,3), next step is
(r,c) = (4,5)
"""
import collections

n = 5 # board size is nxn

def solver(n, X, solution):
    if len(solution) == n * n:
        return True
    else:
        if len(solution) == 0:
            # start with making the 1st step at any square
            for r in range(n):
                for c in range(n):
                    rc = (r, c)
                    solution.append(rc)
                    X.add(rc)
                    flag = solver(n, X, solution)
                    if flag:
                        return True
                    else:
                        solution.pop()
                        X.remove(rc)
            return False
        else:
            moves = [(-1,+2), (-2,+1), (-2,-1), (-1,-2),
                     (+1,-2), (+2,-1), (+2,+1), (+1,+2)]
            for (dr, dc) in moves:
                r0, c0 = solution[-1]
                r1, c1 = r0 + dr, c0 + dc
                if 0 <= r1 < n and 0 <= c1 < n:
                    rc = (r1, c1)
                    if rc not in X:
                        solution.append(rc)
                        X.add(rc)
                        flag = solver(n, X, solution)
                        if flag:
                            return True
                        else:
                            solution.pop()
                            X.remove(rc)
            return False
                

X = set()
solution = collections.deque()
flag = solver(n, X, solution)
if not flag:
    print("no solution")
else:
    print("solution found")

mat = [[0 for c in range(n)] for r in range(n)]
for i,(r,c) in enumerate(solution):
    mat[r][c] = i

for c in range(n):
    print("+--", end='')
print("+")
for row in mat:
    print("|", end='')
    for c in row:
        print("%2s|" % c, end='')
    print()
    for c in range(n):
        print("+--", end='')
    print("+")
