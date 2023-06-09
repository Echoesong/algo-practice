var twoSum = function(nums, target) {
    for(i=0; i<nums.length; i++){
        for(j=0; j<nums.length; j++){
            if(nums[i] == nums[j]){
                j++
            }
            if(nums[i] + nums[j] == target){
                let result = [i, j]
                return result
            }
            console.log('hello world')
        }
    }

};
nums = [3,2,4], target = 6
console.log(twoSum(nums, target))