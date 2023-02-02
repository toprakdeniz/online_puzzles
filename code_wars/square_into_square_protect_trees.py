def decompose(n):
    result = []
    def promising( left, leap):
        if leap * (leap + 1) * ( leap * 2 + 1)/6 >= left:
            return True
        else:
            return False
    
    def backtracking(left, leap):
        sq_leap = leap * leap
        if sq_leap == left:
            result.append(leap)
            return True
        elif sq_leap < left:
            if not promising(left, leap):
                return False
            else:
                for i in range(1,leap):
                    if backtracking(left - sq_leap, leap - i):
                        result.append(leap)
                        return True
                return False
        else:
            return False
    backtracking( n*n, n-1)
    return result if result else None
