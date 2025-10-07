class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in store:
                return True
            store[x] = i
        return False
