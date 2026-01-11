class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sToT = {}
        tToS = {}

        for i in range(len(s)):
            if t[i] not in tToS and s[i] not in sToT:
                tToS[t[i]] = s[i]
                sToT[s[i]] = t[i]
            elif t[i] not in tToS or s[i] not in sToT:
                return False
            elif tToS[t[i]] != s[i]:
                return False

        return True
