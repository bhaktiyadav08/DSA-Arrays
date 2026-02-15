from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        # Pad with '0' and iterate from right to left
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            total = int(x) + int(y) + carry
            result.append(str(total % 2))
            carry = total // 2
        
        if carry:
            result.append('1')
        
        return ''.join(reversed(result))