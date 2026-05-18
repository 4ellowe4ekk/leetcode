class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        chisla = {}

        for chislo in nums:

            if chislo in chisla:
                chisla[chislo] += 1
            else:
                chisla[chislo] = 1

        for i in chisla:

            if chisla[i] >= 2:
                return True
            
        return False