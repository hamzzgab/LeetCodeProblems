class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        listS = []
        for val in s:
            listS.append(s.index(val))

        listT = []
        for val in t:
            listT.append(t.index(val))

        return listS == listT