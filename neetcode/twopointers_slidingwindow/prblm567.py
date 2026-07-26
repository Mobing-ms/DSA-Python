class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        count1 = {}
        count2 = {}

        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1

        l = 0

        for r in range(n2):

            count2[s2[r]] = count2.get(s2[r], 0) + 1

            if r - l + 1 > n1:
                count2[s2[l]] -= 1

                if count2[s2[l]] == 0:
                    del count2[s2[l]]

                l += 1
            if count1 == count2:
                return True

        return False