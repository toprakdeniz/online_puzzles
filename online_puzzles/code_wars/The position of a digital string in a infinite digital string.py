# Two parts to solution
# calculate smallest n and offet from the string
# calculate index of n. element and add offset 

def find_position(string):
    for i in range(len(string)):
        n, offset = find_smallest_sequential_number(string, i+1)
        if n is not None:
            position = calculate_position(n, offset)
            return position
    start_with_one =  int("1" + string)      
    if control(string, start_with_one) != -1:
        return calculate_position(start_with_one, 1)
    raise Exception("Not found")


def calculate_position(n, offset):
    result = 0
    n_digits = len(str(n))
    s = 9
    for i in range(1, n_digits):
        result += s * i
        s *= 10
    result += (n - 10**(n_digits-1)) * n_digits
    result += offset
    return result


def control(string, number):
    s = ""
    if number <= 0:
        return -1 
    while len(s) < len(string):
        s += str(number)
        number += 1
    s += str(number)
    return s.find(string)

    
    
def find_smallest_sequential_number(string, digit_count):
    # s[1+i : digit_count + i] 
    # if digit_count + i > len(string)
    #  s[1+i : len(string)] + s[0 : digit_count + i - len(string)]
    result = []

    # first digit_count 
    if control(string, int(string[:digit_count])) == 0:
        result.append((int(string[:digit_count]), 0))        
    
    # before the first digit
    for i in range(1, digit_count):
        s = int(string[digit_count - i : digit_count] + string[:digit_count - i])
        index = control(string, s)
        if index != -1:
            result.append((s, index))
    
    # after the last digit
    for i in range(1, digit_count):
        if i + digit_count < len(string):
            s = int(string[i : digit_count + i])

            index = control(string, s)
            if index != -1:
                result.append((s, index))
        else:
            s = int(string[i : len(string)] + string[: i + digit_count - len(string)]) - 1
            index = control(string, s)
            if index != -1:
                result.append((s, index))
            s = int(string[i : len(string)] + "0" * (i + digit_count - len(string))) - 1
            index = control(string, s)
            if index != -1:
                result.append((s, index))
    if not result:
        return None, None
    return min(result, key=lambda x: x[0])


class Test:
    def __init__(self):
        self.test_count = 0
        self.error_count = 0
    def assert_equals(self, a, b, *args, **kwargs):
        self.test_count += 1
        if a != b:
            self.error_count += 1
            print(self.test_count, self.error_count, "result" ,a," actual", b, *args, **kwargs)
            
# def calculate_number(n):
#     result = 0
#     while n  > 0:
#         result += 1
#         n -= len(str(result))
#     return result
# print(calculate_number(168))

test = Test()
test.assert_equals(find_position("456") , 3,"...3456...") # 1
test.assert_equals(find_position("454") , 79,"...444546...") # 2
test.assert_equals(find_position("455") , 98,"...545556...") # 3
test.assert_equals(find_position("910") , 8,"...7891011...") # 4
test.assert_equals(find_position("9100") , 188,"...9899100...") # 5
test.assert_equals(find_position("99100") , 187,"...9899100...") # 6
test.assert_equals(find_position("00101") , 190,"...9899100...") # 7
test.assert_equals(find_position("001") , 190,"...9899100...")  # 8
test.assert_equals(find_position("00") , 190,"...9899100...") # 9
test.assert_equals(find_position("123456789") , 0) # 10 
test.assert_equals(find_position("1234567891") , 0) # 11 
test.assert_equals(find_position("123456798") , 1000000071) # 12 
test.assert_equals(find_position("10") , 9) # 13 
test.assert_equals(find_position("53635") , 13034) # 14
test.assert_equals(find_position("040") , 1091) # 15
test.assert_equals(find_position("11") , 11) # 16 
test.assert_equals(find_position("99") , 168) # 17 
test.assert_equals(find_position("667") , 122) # 18
test.assert_equals(find_position("0404") , 15050) # 19
test.assert_equals(find_position("949225100") , 382689688) # 20
test.assert_equals(find_position("58257860625") , 24674951477) # 21
test.assert_equals(find_position("3999589058124") , 6957586376885) # 22
test.assert_equals(find_position("555899959741198") , 1686722738828503) # 23
test.assert_equals(find_position("01") , 10) # 24 
test.assert_equals(find_position("091") , 170) # 25
test.assert_equals(find_position("0910") , 2927) # 26
test.assert_equals(find_position("0991") , 2617) # 27
test.assert_equals(find_position("09910") , 2617) # 28
test.assert_equals(find_position("09991") , 35286) # 29