class Solution:
    def twoSum(self, nums: list, target: int) -> list:

        checkMap = {}

        for i in range(len(nums)):

            if (target - nums[i] in checkMap):

                return [i, checkMap[target - nums[i]]]

            else:
                checkMap[nums[i]] = i





sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums,target))