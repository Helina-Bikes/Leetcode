class Solution:
    def singleNumber(self, nums):
        # Using XOR to find the single number
        result = 0
        for num in nums:
            result ^= num
        return result

# Example usage:
# nums = [4, 3, 2, 4, 1, 2, 3]
# print(Solution().singleNumber(nums))
