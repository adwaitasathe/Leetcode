class Solution:
    def rotate(self, nums: list, k :int) -> None:
        nums_length = len(nums)
        for k in range(k):
            nums.insert(0,nums[nums_length - 1])
            nums.pop()

        print(nums)

    def rotate1(self, nums: list, k: int) -> None:

        nums = nums[len(nums) -k :] + a[0:len(nums) - k ]
        print(nums)

    def rotate2(self, nums: list, k: int) -> None:

        nums = nums[len(nums) -k :] + a[0:len(nums) - k ]
        print(nums)





sol = Solution()
a = [1,2,3,4,5,6,7]
k = 3
print(sol.rotate(a,k))