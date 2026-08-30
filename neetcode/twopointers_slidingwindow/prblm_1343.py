class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        r,l,count,ans = 0,0,0,0
        for r in range(len(arr)):
            count += arr[r]

            if r-l+1 == k:
                if count/k >= threshold:
                    ans += 1

                count = count - arr[l]
                l += 1

        return ans
