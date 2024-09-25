'''
input: string
output: string

Clarifications
- alphabet can be lowercase and uppercase
- if there is one character, return the character itself 

Test Cases
"hello" -> "holle" (e, o are the vowels. reverse them)
"aeiou" -> "uoiea" 
"a" -> "a"

Approach 1) 2-pass
            1st pass - go through once, store the vowels
            2nd pass - go through the string again, replace the vowels

Approach 2) two pointer. 

Plan
- define the function taking string as parameter
    - convert given string into the list
    - initialize vowels list and j to 0
    - iterate through the string:
        - if the current string is vowels, add it to the vowels list
    - iterate through the string again in the reverse order
        - if the current string is vowels, replace the character with the alphabet at j
        - increase the pointer j by 1
    - convert the list into string and return

TC: O(2N), SC: O(N)
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = []
        j = 0

        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                vowels.append(s[i])

        for i in range(len(s) - 1, -1, -1):
            if s[i] in 'aeiouAEIOU':
                s[i] = vowels[j]
                j += 1
        
        return ''.join(s)
