class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currNum = nums[0]
        currCount = 1

        for i in range(1, len(nums)):
            if currCount == 0:
                currNum = nums[i]
                currCount = 1
            elif currNum == nums[i]:
                currCount += 1
            else:
                currCount -= 1

        return currNum
