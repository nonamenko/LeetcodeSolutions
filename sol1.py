from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

    def twoSumAllPairs(self, nums: List[int], target: int) -> List[List[int]]:
        seen = {}
        pairs = []
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                for j in seen[complement]:
                    pairs.append([j, i])
            if num in seen:
                seen[num].append(i)
            else:
                seen[num] = [i]
        return pairs
