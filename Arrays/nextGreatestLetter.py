class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Binary search approach
        left, right = 0, len(letters) - 1
        
        # If target is greater than or equal to the last letter,
        # return the first letter (wrap around)
        if target >= letters[-1]:
            return letters[0]
        
        while left < right:
            mid = left + (right - left) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return letters[left]