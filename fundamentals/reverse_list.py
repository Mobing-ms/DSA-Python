class Solution:
    def reverse_list(self,arr):
        new_list = []
        i = 0
        for i in range(len(arr)):
            i = i+1
            new_list.append(arr[-i])
        return new_list

sol = Solution()
out_list = sol.reverse_list([1,2,3,4,5])
print(out_list)