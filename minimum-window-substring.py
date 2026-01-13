class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substringCharCount = {}
        for c in t:
            substringCharCount[c] = substringCharCount.get(c, 0) + 1

        requiredCharCount = len(substringCharCount)
        validCharCount = 0

        l = 0
        windowCharCount = {}

        minSubstringStart = 0
        minSubstringEnd = 0
        currSubstringStart = 0
        currSubstringEnd = 0
        validStr = False

        for r in range(len(s)):
            if s[r] in substringCharCount:
                windowCharCount[s[r]] = windowCharCount.get(s[r], 0) + 1
                currSubstringEnd += 1

                if windowCharCount[s[r]] == substringCharCount[s[r]]:
                    validCharCount += 1

                # Update left pointer
                while l < len(s) and (
                    s[l] not in substringCharCount or
                    windowCharCount.get(s[l], 0) > substringCharCount.get(s[l], 0)
                ):
                    if s[l] in windowCharCount:
                        if windowCharCount[s[l]] == substringCharCount[s[l]]:
                            validCharCount -= 1
                        windowCharCount[s[l]] -= 1
                    l += 1
                    currSubstringStart += 1

                # Check if substring is valid
                if validCharCount == requiredCharCount and (
                    not validStr or
                    currSubstringEnd - currSubstringStart < minSubstringEnd - minSubstringStart
                ):
                    validStr = True
                    minSubstringStart = currSubstringStart
                    minSubstringEnd = currSubstringEnd

            elif currSubstringEnd - currSubstringStart > 0:
                currSubstringEnd += 1

            if currSubstringEnd - currSubstringStart == 0:
                l += 1
                currSubstringStart += 1
                currSubstringEnd += 1

        return s[minSubstringStart:minSubstringEnd] if validStr else ""
