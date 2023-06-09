// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
console.log('hello world')
function Solution(nums){
    let cache = []
    for(i=0; i<nums.length; i++){
        console.log("num at index: " + nums[i])
        if(cache.includes(nums[i])){
            return true
        } else{
            cache.push(nums[i])
        }
        if(cache.length === nums.length){
            return false
        }
    }
}

nums = [1,1,1,3,3,4,3,2,4,2]
console.log(Solution(nums))