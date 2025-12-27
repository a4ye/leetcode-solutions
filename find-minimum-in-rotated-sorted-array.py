class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findOffset(nums, l, r):
            while l != r:
                mid = l + (r - l) // 2
                if nums[mid] > nums[-1]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        return nums[findOffset(nums, 0, len(nums) - 1)]
