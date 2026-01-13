class Solution:
    def separateSquares(self, squares):
        if not squares:
            return 0.0
        
        min_y = float('inf')
        max_y = float('-inf')
        
        for x, y, l in squares:
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
        
        def area_above(line_y):
            total = 0.0
            for x, y, l in squares:
                if y + l > line_y:
                    height = y + l - max(y, line_y)
                    total += height * l
            return total
        
        def area_below(line_y):
            total = 0.0
            for x, y, l in squares:
                if y < line_y:
                    height = min(y + l, line_y) - y
                    total += height * l
            return total
        
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2.0
        
        left, right = min_y, max_y
        
        for _ in range(100):
            mid = (left + right) / 2.0
            below = area_below(mid)
            
            if below < target:
                left = mid
            else:
                right = mid
        
        return round((left + right) / 2.0, 5)