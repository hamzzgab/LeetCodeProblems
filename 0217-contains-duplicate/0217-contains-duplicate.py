class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hash = {}
        for i, n in enumerate(nums):
            if n in hash:
                return True
                break
            hash[n] = i
        return False