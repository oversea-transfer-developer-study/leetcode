var compresss = function (chars) {
    
    
    let write = 0; //placing the compressed characters in the list 
    let read = 0; //iterating through the list.

    while (read < chars.length) {
        let char = chars[read];
        let count = 0;

        // Count the number of consecutive characters
        while (read < chars.length && chars[read] === char) {
            count++;
            read++;
        }

        //Replace the character at the write position in the list with the current character.
        chars[write] = char;
        //move pointer
        write++;
        if (count > 1) {
            //If the character repeats more than once, convert the count to a string and add each digit to the list at subsequent positions.
            for (let digit of String(count)) {
                chars[write] = digit;
                write++;
            }
        }
    }

    //return write;

    console.log(chars)
};