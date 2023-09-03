class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = {}
        for idx, num in enumerate(nums):
            if num in hash:
                return True
                break
            hash[num] = idx
        return False