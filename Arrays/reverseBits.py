class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1           # Make space for next bit
            result |= n & 1        # Add least significant bit of n
            n >>= 1                # Remove least significant bit from n
        return result