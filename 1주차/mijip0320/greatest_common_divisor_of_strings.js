var gcdOfStrings = function (str1, str2) {
   // handle the base case
    if (str1 + str2 !== str2 + str1) return '';
    let a = str1.length
    let b = str2.length

    // loop (divide) until you find the 
    // highest common factor (length of string)
    
    while (b) {
        
        let temp = b
        b = a % b
        a = temp

        console.log(b)
    }
    console.log(str1.substring(0, a));
  
};