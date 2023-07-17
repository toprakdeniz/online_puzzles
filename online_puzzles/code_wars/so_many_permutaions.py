# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
# my first solution
# STDERR Max buffer size Reached (1.5MiB)

from copy import deepcopy

def permutations(s):
    result = []
    meta = string_to_meta(s)
    stack = [meta]
    while stack:
        meta = stack.pop()
        if meta[1]:
            stack.extend(create_children_meta(meta))
        else:
            result.append(meta[0])
    return result


def string_to_meta(s):
    M = {}
    for c in s:
        if c in M:
            M[c] += 1
        else:
            M[c] = 1
    M = [[k,v] for k,v in M.items()]
    return ["", M]


def create_children_meta(meta):
    result = []
    S, M = meta
    for i,m in enumerate(M):
        _M = deepcopy(M)
        _S = S + m[0]
        if m[1] == 1:
            _M.pop(i)
        else:
            _M[i][1] -= 1
        yield (_S,_M)
        
# ----------------------------------------------------------------
# Thinking about useing generators.
# It would be like: 
# 1-get the last generator. 
# 2-yield one value:
#  2.1- if it is a meta, append it to the stack go to 1
#  2.2- if it is a string, append it to the result, pop the stack go to 1
#  2.3- if it is None, pop the stack go to 1
# 3- if the stack is empty, return the result
# I realise that this solution only puts indexing complexity to the generator
# and it feels like recursion. 



