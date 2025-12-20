class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        log = math.log(n, 2)
        return 2 ** int(log) == n
