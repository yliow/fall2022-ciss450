"""Informally...
Create a proposition:
john_is_tall = Prop_Atom("john_is_tall")
tom_is_smart = Prop_Atom("tom_is_smart")
P = AND(john_is_tall, tom_is_smart)          # i.e., logical AND operator
also OR, NOT, IMPLIES, BICOND, ...

in math325, given propositions P, Q, R
what is the truth table for P ^ Q -> P v ~R.
Interested in knowing WHEN P ^ Q -> P v ~R is true in terms of P, Q, R.
This is called the SAT problem
We need to have
 SAT(P ^ Q -> P v ~R) -> [[P, TRUE], [Q, FALSE], [R, TRUE], ......]

Grammar for propositional logic:
"""

class Atom:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

TRUE = Atom("TRUE")
FALSE = Atom("FALSE")

class AND:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return "(%s AND %s)" % (self.left, self.right)

def EVAL(e, assignment):
    if isinstance(e, AND):
        left = e.left
        for a, b in assignment:
            print("a.name:", a.name)
            if a.name == left.name:
                print("match! ... substitute")
                left = b
                break
        right = e.right
        for a, b in assignment:
            print("a.name:", a.name)
            if a.name == right.name:
                print("match! ... substitute")
                right = b
                break
        if left.name == TRUE.name and \
           right.name == TRUE.name:
            return TRUE
        elif left.name == FALSE.name:
            return FALSE
        elif right.name == FALSE.name:
            return FALSE
        else:
            return AND(left, right)
    else:
        print("WRONG")
    return

if __name__ == '__main__':
    
    john_is_tall = Atom("john_is_tall")
    print(john_is_tall)
    it_is_raining = Atom("it_is_raining")
    print(it_is_raining)
    P = AND(john_is_tall, it_is_raining)
    print(P)
    R = EVAL(P, [(it_is_raining, TRUE),
                 (john_is_tall, TRUE)])
    print(R) # AND(john_is_tall, TRUE)
