class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = max(min_index, max_index) + 1
        right = n - min(min_index, max_index)

        both = min_index + 1 + (n - max_index)
        both2 = max_index + 1 + (n - min_index)

        return min(left, right, both, both2)