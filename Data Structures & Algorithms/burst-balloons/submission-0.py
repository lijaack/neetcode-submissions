class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def dfs(arr):
            if len(arr) == 0:
                return 0
            arr_tup = tuple(arr)

            if arr_tup in dp:
                return dp[arr_tup]

            cur_max = 0

            for j in range(len(arr)):
                arr_copy = arr.copy()
                left = 1
                right = 1

                if j > 0:
                    left = arr_copy[j-1]
                if j < len(arr_copy)-1:
                    right = arr_copy[j+1]

                pop = left * arr_copy[j] * right
                arr_copy.pop(j)
                cur_max = max(dfs(arr_copy) + pop, cur_max)


            dp[arr_tup] = cur_max
            #need to retun a max 
            return dp[arr_tup]
    
        

        return dfs(nums.copy())