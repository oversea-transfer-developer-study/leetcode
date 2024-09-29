# 1. Problem 

# 2. Test case
# 	Input: the sky is blue
# 	Output: blue is sky the
			
# 	Input: "  hello world  "
# 	Output: world hello
		
	
# 3. Plan
# Pointer where we write the compressed string
# Pointer for reading through chars array
# Count the occurrences of the current character
# Write the character to the `write` pointer
# If the count is more than 1, write the count as well
	
	
# Time Complexity: O(n)
# Space Complexity: O(1)

def compress(chars):
    write = 0  
    read = 0 
    
    while read < len(chars):
        char = chars[read]  
        count = 0
        
       
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        
        chars[write] = char
        write += 1
        
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    
    return write


