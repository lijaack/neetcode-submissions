class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
                #[1,3,7,9,12,13] target =  12
                left = 0
                right = len(numbers)-1

                while left < right:

                    if numbers[left] + numbers[right] == target:
                        return [left+1, right+1]                

                    #if sum is big right goes down
                    if numbers[left] + numbers[right] > target:
                        right -= 1
                    #if sum is small left goes up
                    else:
                        left +=1
                    


