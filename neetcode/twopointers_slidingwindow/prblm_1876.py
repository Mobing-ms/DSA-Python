class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = {}
        l = 0
        ans = 0

        for r in range(len(s)):

            counter[s[r]] = counter.get(s[r], 0) + 1

            if r - l + 1 == 3:

                if len(counter) == 3:
                    ans += 1

                counter[s[l]] -= 1

                if counter[s[l]] == 0:
                    del counter[s[l]]

                l += 1

        return ans
