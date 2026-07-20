class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path):
            #base case where length of the path and length of the nums become same 
            if len(path) == len(nums):
                result.append(path[:])
                return
                
            #constrains
            for num in nums:
                if num in path:
                    continue 
                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return res