class Solution:
    def isSorted(self, arr):
        
        temp = arr[0]
        
        for i in range(len(arr)):
            if temp <= arr[i]:
                temp = arr[i]
                continue
            else:
                return False
        else:
            return True
                
sol = Solution()
out = sol.isSorted([1,2,3,4,5,6,7])
print(out)