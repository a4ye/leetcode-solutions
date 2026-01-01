class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        for i in range(len(nums)):
            # If number is same as previous, skip it because it will result in a duplicate triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if  total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    solutions.append([nums[i], nums[l], nums[r]])
                    
                    # Prevent duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return solutions
