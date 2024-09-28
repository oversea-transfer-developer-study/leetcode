var kidsWithCandies = function(candies, extraCandies) {
    let result = Array.from(candies, (x) => false);

    for (let i = 0; i < candies.length; i++){
        const sum = candies[i] + extraCandies;
         
        //filtering numbers that are bigger than sum
        const temp = candies.filter((el, index) => sum < el ? el : '')
        //if there are no numbers that are bigger than sum, it means it is the greatest number
        if (temp.length === 0) {
            result[i] = true
        }
       
       
    }

    console.log(result)
};