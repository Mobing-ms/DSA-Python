#Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x.
#This element is called the floor of x. If such an element does not exist, return -1

class Solution:
    def findFloor(self, arr, x):
        left,right = 0,len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] <= x:
                left = mid + 1

            if arr[mid] > x:
                right = mid - 1

        return left - 1

sol = Solution()
out = sol.findFloor([1,2,8,10,10,12,19],0)
print("Index is: " ,out)