class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashmap = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        for num, count in hashmap.items():
            freq[count].append(num)

        res = []
        for idx in range(len(freq)-1, -1, -1):
            for val in freq[idx]:
                res.append(val)
                if len(res) == k:
                    return res