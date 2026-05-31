class Solution(object):
    def lengthOfLastWord(self, s):
        sl = s.split()
        return len(sl[-1])
