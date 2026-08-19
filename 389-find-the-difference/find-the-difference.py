class Solution(object):
    def findTheDifference(self, s, t):
        for ch in t:
            if ch not in s:
                return ch
            s = s.replace(ch, "", 1)