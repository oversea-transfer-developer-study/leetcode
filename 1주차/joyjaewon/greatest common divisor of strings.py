'''
input: 2 strings
output: string - largest string x which divides both string1 and 2

Clarifications
- all uppercase, non-empty
- length of the strings can be different

Test Cases
ABCABC, ABC -> ABC
LEET, CODE -> ''
A, A -> A

Approach 1) try all substrings of str1 and check if it divides both str1 and str2 => O(N^2)
Approach 2) use gcd
'''

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]
