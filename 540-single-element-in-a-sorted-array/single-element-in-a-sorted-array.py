class Solution(object):
    def singleNonDuplicate(self, nums):
        n = len(nums)
        if n == 1 :
                return nums[0]
        low = 1
        high = n-2
        if nums[low -1] != nums[low] :
            return nums[low - 1]
        if nums[high + 1] != nums[high] :
            return nums[high + 1]
        while(low <= high ) :
            mid =(low+high)//2
            if (nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]):
                return nums[mid]
            # if element is on right half
            if(mid % 2 == 0 and nums[mid+1]==nums[mid]) or (mid % 2 == 1 and nums[mid-1]==nums[mid]) :
                low = mid+1
            else :
                high = mid -1
