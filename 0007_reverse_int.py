# Problem statement - https://leetcode.com/problems/reverse-integer/


def reverse(x):
    if x < 0:
        y = 0-x
        strVal = str(y)
    else:
        strVal = str(x)
    if x < ((-2)**31):
        return 0
    if x>= (2**31):
        return 0
    
    digits = [digit for digit in strVal]

    outputStr = ''
    for i in range(len(digits)):
        outputStr += digits.pop()

    output = int(outputStr)
    
    if output < ((-2)**31):
        return 0
    if output>= (2**31):
        return 0 
    if x < 0:
        return (0-output)

    return output