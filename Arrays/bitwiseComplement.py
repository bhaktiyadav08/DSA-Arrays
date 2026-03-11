class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        
        # Create a mask of 1s with the same bit-length as n
        # e.g., if n = 5 (101), mask = 7 (111)
        mask = (1 << n.bit_length()) - 1
        
        # XORing n with the mask flips all bits
        return n ^ mask
