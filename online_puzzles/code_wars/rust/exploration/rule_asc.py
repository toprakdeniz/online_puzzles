def rule_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        print(a,k, x, y)
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]
        
n = 10

for i in rule_asc(n):
    print(i)

# states 
# 1) v[k-1] += v[k]; v[k] = 0
# 2) v[k-1] += 1; v[k] -= 1 until v[k] < v[k-1] -1
#   3) divide v[k]  
