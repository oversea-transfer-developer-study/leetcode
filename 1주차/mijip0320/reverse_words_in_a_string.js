var reverseWords = function (s) {
    let revStr = "";

    //split s with blanks and reverse, and filter that are not blanks
    const splitString = s.split(' ').reverse().filter((el) => el !== "");
  
    for (let i = 0; i < splitString.length; i++){
        if (i !== 0) {
            //when it is the second word, add with a blank
            revStr += ' ' + splitString[i];

        } else {
            //when it is the first word, just add the word
            revStr += splitString[0]
        }
    }

    console.log(revStr)
};
