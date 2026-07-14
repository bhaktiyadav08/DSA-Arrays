class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        prev_end = 0
        
        for _, end in intervals:
            # If current end extends past the maximum previous end, it's not covered
            if end > prev_end:
                count += 1
                prev_end = end
                
        return count
