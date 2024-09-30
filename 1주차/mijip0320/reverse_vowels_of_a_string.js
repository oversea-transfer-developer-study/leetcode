var reverseVowels = function(s) {
   const vowels = 'aAeEiIoOuU';
    let vow = ""; //vowels that are included in s
    let i = 0;
    let revStr = '';

    for (let c of s) {
      if(vowels.includes(c)){
            vow += c;
        }
    }

    //reverse
    vow = vow.split('').reverse().join('')
    for (let char of s) {
        if (vowels.includes(char)) {
            revStr += vow[i] //add vowel to revStr
            i++
        } else {
            revStr += char //add letter to revStr
        }
    }
    
    return revStr;
};