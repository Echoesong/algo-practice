# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# OKay so we can't use a sorting algorithm because that's higher than linear time complexity
# Sort it ourself? - can you sort it better than the default sort algorithm?
# Add numbers to a set? - nope, doesn't sort
def longest_consecutive(nums):
    my_list = []
    my_comparison = []
    for num in nums:
        if not num in my_list:
            my_list.append(num)
    print(my_list)

    pass

nums = [0,3,7,2,5,8,4,6,0,1]

longest_consecutive(nums)