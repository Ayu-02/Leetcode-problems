class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        sum=[]
        for i in range(nums[0],nums[-1]+1):
           if i not in nums:
            sum.append(i)

        return sum


