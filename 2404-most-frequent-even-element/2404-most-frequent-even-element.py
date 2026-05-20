class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        chisla = {}
        itog = -1
        m = 0

        for num in nums:
            if num % 2 == 0:
                if num in chisla:
                    chisla[num] += 1
                else:
                    chisla[num] = 1

        for chislo, x in chisla.items():

            if x > m:
                itog = chislo
                m = x

            elif x == m:
                itog = min(chislo, itog)

        return itog             