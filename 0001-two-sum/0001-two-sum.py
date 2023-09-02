class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash = {}
        for i, n in enumerate(nums):
            diff = (target - n)
            if diff not in hash:
                hash[n] = i
            else:
                return [hash[diff], i]