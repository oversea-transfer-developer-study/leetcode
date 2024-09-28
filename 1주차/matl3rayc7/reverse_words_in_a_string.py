class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        str = ''
        for i in range(0, len(x)):
            if i != len(x) -1:
                str += x[len(x)-1-i] + ' '
            else:
                str += x[len(x)-1-i]
        return str
        