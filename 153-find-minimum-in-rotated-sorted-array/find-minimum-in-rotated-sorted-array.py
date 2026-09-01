class Solution(object):
    def findMin(self, nums):
        low = 0 
        high = len(nums) - 1
        ans = float('inf')
        while(low <= high ):
            mid = (low+high)//2
            #if entire space is sorted
            if nums[low] <= nums[high] :
                ans = min(nums[low],ans) 
                break
            #if left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] < ans :
                    ans = nums[low]
                low = mid + 1 # minimum lies in right
            else :
                #if  right half is sorted
                ans =  min(ans,nums[mid])
                high = mid # minimum lies in left
        return ans
                
