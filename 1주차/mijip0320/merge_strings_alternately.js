var mergeAlternately = function(word1, word2) {
    if (word1 !== '' && word2 !== '') {
        let result = "";
        for (let i = 0; i < word1.length; i++){

            //merge first letter
            result += word1[i];
            //if there is letter to merge from word2, merge
            if(word2[i])result += word2[i];
        }

        //if word2 is bigger than word1, merge the leftovers
        if (word2.length > word1.length) {
            let leftovers = word2.substring(word1.length, word2.length);
            result += leftovers;
        }  
        console.log(result)
        
    }
};