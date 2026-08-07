class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l=0
        r=0

        stack= deque()
        
        while r < len(nums):
            #we add index to the stack. we check the stack[-1] vs curr number. whatever is higher we append it
            while stack and nums[stack[-1]]< nums[r]:
                stack.pop()
            stack.append(r)
            if stack[0] < l:
                stack.popleft()

            if r + 1 >= k:
                res.append(nums[stack[0]])
                l+=1
            r+=1

        return res            
