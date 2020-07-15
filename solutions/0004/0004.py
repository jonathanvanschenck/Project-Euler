"""


Created By: Jonathan D. B. Van Schenck

Method:
Construct the palendromic numbers in decreasing size which could possibly factor
into two n-digit numbers. Actually factor it and see if it DOES factor into
two n-digit numbers.

"""

from math import sqrt

def split(number):
    # Produces the paired factors of a number:
    #  Example 12 -> [[1, 12], [2, 6], [3, 4]]
    splits = [[1,number]]
    sr = int(sqrt(number))
    for factor in range(2,sr+1):
        if number % factor == 0:
            splits.append([factor, number // factor])
    return splits

def run_2_digit():
    for a in range(9,-1,-1):
        for b in range(9,-1,-1):
            number = a*1001 + b*110
            q,r = split(number)[-1]
            if q>9 and q<100 and r>9 and r<100:
                return number,q,r

def run_3_digit():
    # Construct all potentially 3-digit factorable palendromic numbers
    for a in range(9,-1,-1):
        for b in range(9,-1,-1):
            for c in range(9,-1,-1):
                number = a*100001 + b*10010 + c*1100
                # Factor the test palendrome
                #  Note, by construction, if it factors into 2 3-digit numbers,
                #  That will be the last factor pair in our list
                q,r = split(number)[-1]
                # Check if the factors are 3-digits
                if q>99 and q<1000 and r>99 and r<1000:
                    return number,q,r


print(run_3_digit()[0])
