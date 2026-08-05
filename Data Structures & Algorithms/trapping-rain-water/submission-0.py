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
                print('current height change', height[left],height[right])

            if height[left]<height[right]:
                left+=1
                if currHeight-height[left]>0:
                    water += currHeight-height[left]
                    print('add left: ' ,height[left] ,'currheight', currHeight, 'currwater' , water)
            else:
                right-=1
                if currHeight-height[right]>0:
                    water += currHeight-height[right]
                    print('add right: ',height[right] ,'currheight', currHeight, 'currwater' , water)
            #
            #container with most water. +   curHeight water - space
        return water

             
        