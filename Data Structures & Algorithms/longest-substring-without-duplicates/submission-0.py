class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        L = 0
        length = 0

        for R in range(len(s)):
            while s[R] in seen:
                seen.pop(s[L], None)
                L += 1

            seen[s[R]] = R

            if len(seen) > length:
                length = len(seen)

        return length