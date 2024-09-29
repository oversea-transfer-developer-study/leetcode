# 1. Problem 
# Check if two strings can be separated by one character given

	

# 2. Test case
# 	Input: str1 = "ABCABC", str2 = "ABC"
# 	Output: "ABC"
	
# 	Input: str1 = "ABABAB", str2 = "ABAB"
# 	Output: "AB"
# 	Example 3:
	
# 	Input: str1 = "LEET", str2 = "CODE"
# 	Output: ""
	
# 	Input str1 = "", str2 = "ABC"
# 	Output: "ABC"
	
# 3. Plan
# 	Iterate over all possible lengths starting from min_len down to 1
# 	Check if the prefix of length i can generate both strings
	
	
# Time Complexity: O(n1 * n2), where n1 and n2 are the lengths of str1 and str2. In the worst case, we may need to iterate through both strings multiple times.
# Space Complexity: O(1) for storing the prefix.

min_len = min(len(str1), len(str2))
    
for i in range(min_len, 0, -1):
    if len(str1) % i == 0 and len(str2) % i == 0:
        prefix = str1[:i]
        if prefix * (len(str1) // i) == str1 and prefix * (len(str2) // i) == str2:
            return prefix
return ""
