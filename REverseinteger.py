class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        s = str(abs(x))[::-1]          

        limit = "2147483648" if neg else "2147483647"

        if len(s) > 10:
            return 0

        if len(s) == 10 and s > limit:
            return 0

        val = int(s)
        return -val if neg else valclass Solution:
    