def decompose(n):
    from math import sqrt
    stack = []
    def eldest(left, parent):
        son = int(sqrt(left))
        return son if son < parent else parent -1
    def promising(left, x):
        return  x * (x+1) * (2*x+1) >= left*6
        
    stack.append(( n*n, n))
    while stack:
        last = stack[len(stack)-1]
        if last[0] == 0:
            break
        elder = eldest(*last)
        if promising(last[0], elder):
            stack.append((last[0] - elder*elder, elder))
        else:
            stack.pop()
            while stack:
                elder = last[1] - 1
                last = stack[len(stack)-1]
                if  promising(last[0], elder):
                    stack.append((last[0] - elder*elder, elder))
                    break
                last = stack.pop()
    if stack:
        return list(reversed([i[1] for i in stack[1:]]))
    return None
