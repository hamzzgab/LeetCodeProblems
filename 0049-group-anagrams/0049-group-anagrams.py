class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        new = {}

        for idx, string in enumerate(strs):
            val = "".join(sorted(string))
            if val in new:
                new[val].append(string)
            else:
                new[val] = [string]

        for key in new.keys():
            ans.append(new[key])


        return ans
