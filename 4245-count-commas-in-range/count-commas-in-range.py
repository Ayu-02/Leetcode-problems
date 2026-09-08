class Solution(object):
    def countCommas(self, n):
        count = 0
        number = 1000

        while number <= n:
            count += n - number + 1
            number *= 1000

        return count