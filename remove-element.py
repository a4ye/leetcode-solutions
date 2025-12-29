class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
                nums[i] = -1

        changePos = 0
        for i in range(len(nums)):
            if nums[i] == -1:
                changePos += 1
            else:
                nums[i - changePos] = nums[i]

        return len(nums) - k
