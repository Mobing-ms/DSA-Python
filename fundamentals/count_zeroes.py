#Given an array arr of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. 
#Find the count of all the 0's.

class Solution:
    def countZeroes(self, arr):
        left,right = 0,len(arr) - 1

        while left <= right:
            mid = ((left + right) // 2)

            if arr[mid] == 1:
                left = mid + 1
                continue

            if arr[mid] == 0:
                right = mid - 1
                continue
        
        return len(arr) - left

sol = Solution()
out = sol.countZeroes([1,1,1,1,1,0,0,0])
print(out)