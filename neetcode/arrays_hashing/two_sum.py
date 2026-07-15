class Solution:
    seen = dict()
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in nums[i + 1:]:
                return [i,nums.index(diff,i + 1)]

sol = Solution()
out_list = sol.twoSum([3,4,5,6],7)
print(out_list)




                