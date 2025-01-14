class Solution:

    def findMaxAverage(self, nums: list[int], k: int) -> float:
        import math
        from decimal import Decimal

        total = sum(nums[:k])
        maxTotal = total

        for i in range(k, len(nums)):
            # print(maxTotal, total, i)
            total += nums[i] - nums[i - k]
            maxTotal = max(maxTotal, total)
            
        maxAverage = maxTotal / k
        
        # if maxAverage == -math.inf:
        #     maxAverage = nums[0]

        return Decimal(f'{maxAverage:.5f}')

instance = Solution()
maxAverage = instance.findMaxAverage([0, 1, 1, 3, 3], 4)
print(maxAverage)