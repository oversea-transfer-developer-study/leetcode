class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check the lenght of the two strings
        str1len = len(str1)
        str2len = len(str2)

        # Cretate a empty string to be a divider
        div = ""
        ans = ""

        if str1len < str2len:
            times = str2len // str1len
            if str1 * times == str2:
                return str1
            for i in str1:
                div += i
                str1times = str1len // len(div)
                str2times = str2len // len(div)
                if div * str1times == str1 and div * str2times == str2 :
                    ans = div
        else:
            times = str1len // str2len
            if str2 * times == str1:
                return str2
            for i in str2:
                div += i
                str1times = str1len // len(div)
                str2times = str2len // len(div)
                if div * str1times == str1 and div * str2times == str2:
                    ans = div
        return ans
                