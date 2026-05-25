class Solution(object):
    def concatWithReverse(self, nums):
        ans = []
        for i in nums:
            ans.append(i)
        nums.reverse()
        for i in nums:
            ans.append(i)
        return ans