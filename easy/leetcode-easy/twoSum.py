class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in store:
                return [store[target - x], i]
            store[x] = i
