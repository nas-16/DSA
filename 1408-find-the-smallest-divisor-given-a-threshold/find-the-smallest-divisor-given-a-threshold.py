class Solution(object):
    def possibleDivisor(self,nums,threshold,mid):
        cnt = 0
        n = len(nums)
        for i in range(n) :
            cnt +=((nums[i] + mid - 1 )// mid)
        if cnt <= threshold :
            return True
        else :
            return False
    def smallestDivisor(self, nums, threshold):
        low = 1
        high = max(nums)
        while( low <= high ) :
            mid = (low + high ) // 2
            if (self.possibleDivisor(nums,threshold,mid)) :
                high = mid - 1
            else :
                low = mid + 1
        return low
        
        