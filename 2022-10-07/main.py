def successors(state):
    """
    example: state = "A"
    return [("a1", "B"), ...]
    """
    if state == 'A':
        return [('a1', 'B'), ('a2', 'C'), ('a3', 'D')]
    elif state == 'B':
        return [('b1', 'E'), ('b2', 'F'), ('b3', 'G')]
    elif state == 'C':
        return [('d1', 'K'), ('d2', 'L'), ('d3', 'M')]

def terminal_test(state):
    return state in "EFGHIJKLM"

def utility(state):
    return ({'E':3,
             'F':12,
             'G':8,
             'H':2,
             'I':4,
             'J':6,
             'K':14,
             'L':5,
             'M':2,
    }[state])

def f(state, player):
    """
    player must be in ['MAX', 'MIN']
    return the "best" utility value base on player 
    """
    pass
