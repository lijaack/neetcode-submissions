class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #[2,1,5,6,2,3 ]
        #n = 6
        n = len(heights)
        maxArea = 0
        #holds indexes
        stack = []
                        #range = 7. so it will go 0,1,2,3,4,5,6
        for i in range(n + 1):

            #make sure stack has something inside
                            #index is equal to 6 
                                        #or
                                            #check the height[current top in stack] more than height[current position]
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                
                #get previous index 
                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            
            #push current index to the stack
            stack.append(i)
        return maxArea
        