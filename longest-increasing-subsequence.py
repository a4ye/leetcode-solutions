class Solution:
    def insertIndexBinarySearch(self, nums, target, l, r):
        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l

    def lengthOfLIS(self, nums: List[int]) -> int:
        subSequenceLengths = [nums[0]]
        for i in range(len(nums)):
            insertionIndex = self.insertIndexBinarySearch(subSequenceLengths, nums[i], 0, len(subSequenceLengths) - 1)
            if insertionIndex == len(subSequenceLengths):
                subSequenceLengths.append(nums[i])
            else:
                subSequenceLengths[insertionIndex] = nums[i]
        
        return len(subSequenceLengths)
