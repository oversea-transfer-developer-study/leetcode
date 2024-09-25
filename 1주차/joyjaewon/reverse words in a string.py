'''
input: string
output: string - reversed order, concatenated by a single space

Clarifications
- strig will be non-empty
- if there are multiple spaces, we need to reduce it to single space

Test Cases
"the sky is blue  " -> "blue is sky the"
"a" -> "a"

Approach 1) 
use extra space - split the string. reverse, join, return
TC: O(N), SC: O(N)

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return ' '.join(s)