class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = [[nums[i], i] for i in range(len(nums))]
        nums2.sort()
        print(nums2)
        i = 0
        j = 1
        while (i < len(nums2) - 1):
            while (j < len(nums2) and nums2[i][0] + nums2[j][0] < target): j += 1
            if j < len(nums) and nums2[i][0] + nums2[j][0] == target:
                return [nums2[i][1], nums2[j][1]]
            i += 1
            j = i + 1
        return [0, 1]
        