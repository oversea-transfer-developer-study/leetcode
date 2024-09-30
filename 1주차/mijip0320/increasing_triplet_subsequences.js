var increasingTriplet = function (nums) {
    let first=Infinity; //양의 정수
    let second=Infinity;
    for (let third of nums) {
        //console.log(third)
        // If the third is smaller than the first variable then make first = third...
        if(third < first){
            first = third;
        }
        // If the third is in between the first and second then move second to third place...
        else if(third < second && third > first){
            second = third;
        }
        // If the right is greater than the first and second then return true...
        else if(third > second && third > first) return true;
    }
    // After the end of the loop if no such Increasing Triplet Subsequence indices exists then return false...
    return false;
}