class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return ([seen[target - n], i])
            elif n not in seen:
                seen[n] = i​
