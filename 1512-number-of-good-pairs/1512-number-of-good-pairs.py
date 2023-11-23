class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_frequency = {}

        for num in nums:
            if num in num_frequency:
                count += num_frequency[num]
                num_frequency[num] += 1
            else:
                num_frequency[num] = 1

        return count