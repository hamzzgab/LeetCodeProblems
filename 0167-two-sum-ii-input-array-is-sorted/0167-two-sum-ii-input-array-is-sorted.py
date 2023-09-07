class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1

        diff = numbers[i] + numbers[j]

        if diff == target:
            print(numbers[i], '+', numbers[j], '=', diff)
            return [i+1, j+1]
        else:
            while diff != target:                
                diff = numbers[i] + numbers[j]
                if diff > target:
                    j -= 1
                else:
                    i += 1

            return [i, j+1]