class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r

        while l <= r:
            m = (l + r) // 2
            totalHrs = 0

            for p in piles:
                totalHrs += math.ceil(p / m)
            
            if totalHrs <= h:
                best = m
                r = m - 1
            else:
                l = m + 1
        return best
