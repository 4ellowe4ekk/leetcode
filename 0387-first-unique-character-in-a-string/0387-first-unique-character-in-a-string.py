class Solution(object):
    def firstUniqChar(self, s):
        ls = {}

        for i in s:
            if i in ls:
                ls[i] += 1
            else:
                ls[i] = 1

        for i in range(len(s)):
            if ls[s[i]] == 1:
                return i
            
        return -1