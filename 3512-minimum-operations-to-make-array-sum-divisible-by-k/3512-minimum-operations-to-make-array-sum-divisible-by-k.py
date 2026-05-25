class Solution(object):
    def minOperations(self, nums, k):
        s = 0
        kolvo = 0
        for i in nums:
            s += i
        while s % k != 0:
            s -= 1
            kolvo += 1
        return kolvo
        