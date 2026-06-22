class Solution:
    def segregate0and1(self, arr):
        zeros = arr.count(0)
        ones = arr.count(1)

        return [0] * zeros + [1] * ones

sol = Solution()
print(sol.segregate0and1([0,1,0,1,0,0,1,1,1,0]))