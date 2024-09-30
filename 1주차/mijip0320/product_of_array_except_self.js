var productExceptSelf = function (nums) {
    const output = Array(nums.length).fill(1);

    let left = 1;
    //multiply array starting from left side
    for (let i = 0; i < nums.length; i++) {
        output[i] *= left;
        left *= nums[i];
    }

    let right = 1;
    //multiply array from right that was multiplied from left
    for (let i = nums.length - 1; i >= 0; i--) {
        output[i] *= right;
        right *= nums[i];
    }

    return output;    
}