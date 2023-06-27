class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for ele in set(s):
            countS[ele] = s.count(ele)
            countT[ele] = t.count(ele)
            
        return countS == countT