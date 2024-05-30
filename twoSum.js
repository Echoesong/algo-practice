/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(i=0; i<nums.length; i++){
        for(j=0; j<nums.length; j++){
            if(i == j){
                j++
            }
            if(nums[i] + nums[j] == target){
                let result = [i, j]
                return result
            }
        }
    }

};

// Things I had to refresh on: Splice