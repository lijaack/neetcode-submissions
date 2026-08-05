class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1

        currHeight = min(height[right],height[left])
        water = 0

        while left<right:
            #set new height for container
            if min(height[left],height[right]) >currHeight:
                currHeight = min(height[left],height[right])

            if height[left]<height[right]:
                left+=1
                if currHeight-height[left]>0:
                    water += currHeight-height[left]
            else:
                right-=1
                if currHeight-height[right]>0:
                    water += currHeight-height[right]
        return water

             
        