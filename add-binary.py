"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example: 

Input: a = "11", b = "1"
Output: "100"

"""

def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # Get the max string length of a and b
    n = max(len(a), len(b))
    # Fill the 0 to a and b
    a, b = a.zfill(n), b.zfill(n)

    carry, answer = 0, []

    # Iterate backward
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            carry += 1
        if b[i] == 1:
            carry += 1
        if carry % 2 == 0:
            answer.append('0')
        else:
            answer.append('1')
        
        carry //= 2
    if carry == 1:
        answer.append('1')
    answer.reverse()

    return ''.join(answer)