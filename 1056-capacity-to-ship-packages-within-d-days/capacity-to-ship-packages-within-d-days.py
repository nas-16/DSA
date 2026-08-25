class Solution(object):
    def possible(self,weights,days,cap) :
        n = len(weights)
        no_days = 1
        load = 0
        for i in range(n) :
           if (load + weights[i]) > cap :
                no_days += 1
                load = weights[i]
           else :
                load += weights[i]
        if no_days <= days :
            return True
        else :
            return False
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high =sum(weights)
        while (low <= high ) :
            mid = (low + high ) // 2
            if self.possible(weights,days,mid) :
                high = mid - 1
            else :
                low = mid +1
        return low

        