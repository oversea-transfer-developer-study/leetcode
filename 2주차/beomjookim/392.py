class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        if not s: return True

        for c in t:
            if c == s[i]: 
                i += 1
                if i == len(s): return True
        
        return False
