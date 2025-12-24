class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def wordBreakRecursive(s, wordDict):
            if s in memo:
                return False

            for word in wordDict:
                if s.startswith(word):
                    ss = s[len(word):]
                    if len(ss) == 0:
                        return True
                    else:
                        result = wordBreakRecursive(ss, wordDict)
                        if result:
                            return True
                        memo[ss] = False

            return False

        return wordBreakRecursive(s, wordDict)
