#!/usr/bin/python3
"""In a text file, there is a single character H.
   Your text editor can execute only two operations in this file:
   Copy All and Paste. Given a number n,
   write a method that calculates the fewest number of operations
   needed to result in exactly n H characters in the file.

   Prototype: def minOperations(n)
   Returns an integer
   If n is impossible to achieve, return 0
"""


def minOperations(n):
    """Returns the fewest number of operations needed to
       result in exactly n H characters in the file
    """
    if type(n) is not int or n < 2:
        return 0
    res = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            res += i
            n //= i
        i += 1

    if n > 1:
        res += n

    return res
