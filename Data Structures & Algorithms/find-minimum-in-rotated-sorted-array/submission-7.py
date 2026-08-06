class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        smallest=nums[-1]
        #we have to find the smallest number where r<l
        while l <= r:
            mid= (r+l)//2
            if nums[mid] > smallest:
                l=mid+1
            else:
                smallest=nums[mid]
                r=mid-1
        return smallest

        