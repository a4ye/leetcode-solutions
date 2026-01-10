class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mergedR = m + n - 1
        nums2R = n - 1
        nums1R = m - 1

        while nums2R >= 0 and nums1R >= 0:
            if nums2[nums2R] > nums1[nums1R]:
                nums1[mergedR] = nums2[nums2R]
                nums2R -= 1
            else:
                nums1[mergedR] = nums1[nums1R]
                nums1R -= 1
            mergedR -= 1

        while nums2R >= 0:
            nums1[mergedR] = nums2[nums2R]
            nums2R -= 1
            mergedR -= 1

        while nums1R >= 0:
            nums1[mergedR] = nums1[nums1R]
            nums1R -= 1
            mergedR -= 1
