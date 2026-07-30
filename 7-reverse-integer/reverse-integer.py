class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        reverse = 0

        while x != 0:
            digit = x % 10

            # check overflow
            if reverse > INT_MAX // 10:
                return 0

            reverse = reverse * 10 + digit
            x //= 10

        reverse = reverse * sign

        if reverse < INT_MIN or reverse > INT_MAX:
            return 0

        return reverse