class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        l = ['a','A','e','E','i','I','o','O','u','U']

        i = 0
        j = len(s)-1

        i_idx = -1
        j_idx = -1

        while (i <= j):
            if(s[i] in l):
                i_idx = i
            else:
                i += 1

            if(s[j] in l):
                j_idx = j
            else:
                j -= 1
            
            if(i_idx != -1 and j_idx != -1):
                temp = s[j_idx]
                s[j_idx] = s[i_idx]
                s[i_idx] = temp
                i_idx = -1
                j_idx = -1
                i += 1
                j -= 1

        s = ''.join(s)
        return s
        