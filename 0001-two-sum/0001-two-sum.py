class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            diff = (target - num) 

            if (target - num) not in hashmap:
                hashmap[num] = i
            else:                
                return [i, hashmap[diff]]