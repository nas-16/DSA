class Solution(object):
    def no_students(self,nums,mid) :
        cnt = 1
        pages = 0
        for i in range(len(nums)):
            if pages + nums[i] <= mid:
                pages += nums[i]
            else :
                cnt += 1
                pages = nums[i]
        return cnt
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        while(low <= high):
            mid = (low + high) // 2
            students = self.no_students(nums,mid)
            if students > k :
                low = mid + 1
            else :
                high = mid - 1
        return low