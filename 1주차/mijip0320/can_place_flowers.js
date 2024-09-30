//Approach:
//1 . use for loop to see if flowers are planted
//2 . when index === 0 , compare with index + 1
//3 . when index === flowerbed.length - 1, compare with index - 1
//4 . when flower can be planted, decrease count
//5. if count === 0, return true

var canPlaceFlowers = function (flowerbed, n) {
    let result = false;
    let count = n;
     
    if ((flowerbed.length === 1 && flowerbed[0] === 0) || n === 0) {
        result = true;
    } else {
        for (let i = 0; i < flowerbed.length; i++){
        
        if (flowerbed[i] === 0 && ((flowerbed[i + 1] === 0 && flowerbed[i - 1] === 0)
            || (i === 0 && flowerbed[i + 1] === 0)
            || (i === flowerbed.length - 1 && flowerbed[i - 1] === 0))
        ) {
             
            flowerbed[i] = 1;
            count -= 1;
            if (count === 0) break;
            if (count > 0) i = 0;
            
        }
       if (i === flowerbed.length-1) break;
       
    }

   

    if (count === 0) result = true;
 
    }
 
   

    console.log(result);
};