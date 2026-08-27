class Solution(object):
    def possibleSubarrays(self,nums,mid) :
        cnt = 1
        sum = 0
        for i in range(len(nums)):
            if sum + nums[i] <= mid:
                sum += nums[i]
            else :
                cnt += 1
                sum = nums[i]
        return cnt
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        while(low <= high):
            mid = (low + high) // 2
            no_subarrys = self.possibleSubarrays(nums,mid)
            if no_subarrys > k :
                low = mid + 1
            else :
                high = mid - 1
        return low