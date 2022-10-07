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

def opponent(player):
    if player == 'MAX': return 'MIN'
    else: return 'MAX'
    
def f(state, player):
    """
    player must be in ['MAX', 'MIN']
    return the "best" utility value base on player 
    """
    print("f ... state, player:", state, player)
    if terminal_test(state):
        # base case
        ret = utility(state)
        print("f ... state, player:", state, player,
              "... base case ... returning", ret )
        return ret
    else:
        # recursive case
        action_successors = successors(state)
        if player == 'MAX':
            ret = -1
            for action, successor in action_successors:
                v = f(successor, opponent(player))
        else: # 'MIN'
            pass
        
print(successors("A"))
print(terminal_test("A"), terminal_test("G"))
print(utility("G"))

val = f('A', 'MAX')
print("final:", val)
