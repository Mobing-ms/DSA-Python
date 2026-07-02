from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, strs: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(strs):
            j = i

            while strs[j] != "#":
                j += 1

            length = int(strs[i:j])

            decoded.append(strs[j + 1 : j + 1 + length])

            i = j + 1 + length

        return decoded