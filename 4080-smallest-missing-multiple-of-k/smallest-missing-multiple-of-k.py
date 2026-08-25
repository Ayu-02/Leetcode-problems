class Solution(object):
    def missingMultiple(self, nums, k):
        multiples = set(nums)

        multiple = k

        while multiple in multiples:
            multiple += k

        return multiple