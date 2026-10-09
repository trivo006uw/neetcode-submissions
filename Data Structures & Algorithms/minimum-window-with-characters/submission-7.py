class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        need = len(countT)
        have = 0

        l = 0
        resLen = float("infinity")
        res = [-1, -1]

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if resLen > (r - l + 1):
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        

            