class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 1
        maxFreq = 0
        charCount = {}

        for r in range(len(s)):
            if s[r] in charCount:
                charCount[s[r]] += 1
            else:
                charCount[s[r]] = 1

            maxFreq = max(maxFreq, charCount[s[r]])

            while (r - l + 1) - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
