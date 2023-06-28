class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            hash[num] = 1 + hash.get(num, 0)

        for c, n in hash.items():
            freq[n].append(c)

        res = []
        for num in range(len(freq) - 1, 0, -1):
            for n in freq[num]:
                res.append(n)
                if len(res) == k:
                    return res