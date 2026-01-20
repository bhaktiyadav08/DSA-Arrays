class Solution:
    def isValid(self, s):
        stack = []
        bracket_map = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in bracket_map.values():  # opening bracket
                stack.append(char)
            elif char in bracket_map:  # closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # invalid character (optional)
                return False

        return len(stack) == 0
