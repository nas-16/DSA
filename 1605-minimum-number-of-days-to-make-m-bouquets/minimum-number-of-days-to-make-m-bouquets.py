class Solution(object):
    def possible(self,bloomDay,m,k,mid):
        n = len(bloomDay)
        cnt = 0
        no_bouquet = 0
        for i in range(n):
            if bloomDay[i] <= mid :
                cnt += 1
            else :
                no_bouquet += cnt//k
                cnt = 0
        no_bouquet += cnt//k
        if no_bouquet >= m :
            return True
        else :
            return False


    def minDays(self, bloomDay, m, k):
        if m*k > len(bloomDay) :
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while(low <= high ) :
            mid = (low + high ) // 2
            if self.possible(bloomDay,m,k,mid) == True :
                ans = mid
                high = mid - 1
            else :
                low  = mid + 1
        return ans

        