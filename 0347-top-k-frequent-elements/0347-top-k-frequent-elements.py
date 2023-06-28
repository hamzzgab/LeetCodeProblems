class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        print(hash)

        stopper = 0
        ans = []

        for val in sorted(hash.values(), reverse=True):
            value = list(hash.keys())[list(hash.values()).index(val)]
            hash.pop(value)
            ans.append(value)

            stopper += 1
            if stopper == k:
                break

        return ans
        