class Solution(object):

    def hours(self, piles, k):
        total = 0

        for banana in piles:
            total += (banana + k - 1) // k

        return total

    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            total_hours = self.hours(piles, mid)

            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans