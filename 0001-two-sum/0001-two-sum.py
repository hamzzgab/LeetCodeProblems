class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash = {}
        
        for idx, num in enumerate(nums):
            diff = target - num
            
            if diff in hash:
                return [hash[diff], idx]
            else:
                hash[num] = idx