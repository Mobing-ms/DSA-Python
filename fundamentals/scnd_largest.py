"""
Given an array of positive integers arr[], return the second largest element from the array. 
If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element
"""

class Solution:
    def getSecondLargest(self, arr):
        
        if len(arr) >= 2:
            temp = arr[0]
            for i in range(len(arr)):
                if temp <= arr[i]:
                    temp = arr[i]
            new_arr = list(filter(lambda x: x != temp, arr))
            
            if new_arr != []:
                scnd_temp = new_arr[0]
                for i in range(len(new_arr)):
                    if scnd_temp <= new_arr[i]:
                        scnd_temp = new_arr[i]
            return scnd_temp

            else:
                return -1

        else:
            return -1
        

sol = Solution()
out = sol.getSecondLargest([40,30,80,30,80,60])
print(out)