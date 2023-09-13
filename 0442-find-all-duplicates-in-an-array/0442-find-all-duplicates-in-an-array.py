class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash = {}

        for i in nums:
            hash[i] = 1 + hash.get(i, 0)

        res = []
        for k, v in hash.items():
            if v == 2:
                res.append(k)
        return res