class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array with 1's.
        # During the first pass, it will store prefix products.
        # During the second pass, we'll multiply in the suffix products.
        res = [1] * len(nums)

        # Running product of everything to the LEFT of the current index.
        prefix = 1

        # Left-to-right pass: build prefix products.
        for i in range(len(nums)):

            # Store product of all numbers before index i.
            #
            # Example:
            # nums = [2,5,6,8]
            #
            # res becomes:
            # [1,2,10,60]
            res[i] = prefix

            # Update prefix by including the current number
            # for the next iteration.
            prefix *= nums[i]

        # Running product of everything to the RIGHT of the current index.
        postfix = 1

        # Right-to-left pass: multiply suffix products into res.
        for i in range(len(nums) - 1, -1, -1):

            # res[i] currently stores the prefix product.
            # Multiply it by the suffix product to get:
            #
            # product(left of i) * product(right of i)
            res[i] *= postfix

            # Update postfix by including the current number
            # for the next iteration moving left.
            postfix *= nums[i]

        return res            