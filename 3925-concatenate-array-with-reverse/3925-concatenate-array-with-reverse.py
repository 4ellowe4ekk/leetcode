class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        
        ans = []
        for i in nums:
            ans.append(i)
        nums.reverse()
        for i in nums:
            ans.append(i)
        return ans