'''
input: list of strings
output: integer 

Clarifications
- if the count is greater than or equal to 10, it should be split into individual digits.
- should use constant space

Test Cases
['a','a','a','b'] -> ['a','3','b']
['a'] -> ['a']
['a','a','a','a','a','a','a','a','a','a',] -> ['a','1','0']

Plan
- define the function taking the list as a parameter
    - initialize two variables:
        - i to keep track of the current position in the modified list.
        - count to count consecutive occurrences of the same character.
        - iterate over the string:
            - if the current character is the same as the previous one, increment the count.
            - if it’s different, place the previous character at chars[i], and if count > 1, add the count.
                - reset the count to 1.
        - after the loop, handle the last character and its count.

    - return the new length i.

TC: O(N), SC: O(1)
'''
class Solution:
    def compress(self, chars):
        i = 0  
        count = 1 
        
        for right in range(1, len(chars)):
            if chars[right] == chars[right - 1]:
                count += 1
            else:
                chars[i] = chars[right - 1]
                i += 1
                
                if count > 1:
                    for c in str(count):
                        chars[i] = c
                        i += 1
                count = 1 
        
        chars[i] = chars[-1]
        i += 1
        if count > 1:
            for c in str(count):
                chars[i] = c
                i += 1
        
        return i