class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        prevMax = nums[0]
        prevMin = nums[0]
        for i in range(1, len(nums)):
            numI = nums[i]
            oldPrevMax = prevMax
            prevMax = max(max(numI * prevMax, numI * prevMin), numI)
            prevMin = min(min(numI * oldPrevMax, numI * prevMin), numI)

            currMax = max(currMax, prevMax)

        return currMax
