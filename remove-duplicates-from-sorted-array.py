class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        k = 1

        for r in range(1, len(nums)):
            if nums[l] == nums[r]:
                continue
            else:
                k += 1
                nums[l + 1] = nums[r]
                l += 1

        return k
