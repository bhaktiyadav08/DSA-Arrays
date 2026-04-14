class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        # memo[i][j] = min distance for robots starting at i 
        # using factories starting at j
        memo = {}

        def solve(r_idx, f_idx):
            # Base Case: All robots repaired
            if r_idx == n:
                return 0
            # Base Case: No more factories to use
            if f_idx == m:
                return float('inf')
            
            state = (r_idx, f_idx)
            if state in memo:
                return memo[state]
            
            # Option 1: Skip this factory entirely
            res = solve(r_idx, f_idx + 1)
            
            # Option 2: Use this factory for 'k' robots (up to its limit)
            current_dist = 0
            # We try assigning 1, 2, ... up to factory[f_idx][1] robots to this factory
            for k in range(1, factory[f_idx][1] + 1):
                if r_idx + k > n:
                    break
                
                # Add distance of the k-th robot to this factory
                current_dist += abs(robot[r_idx + k - 1] - factory[f_idx][0])
                
                # Recursively solve for the remaining robots and next factory
                sub_res = solve(r_idx + k, f_idx + 1)
                if sub_res != float('inf'):
                    res = min(res, current_dist + sub_res)
            
            memo[state] = res
            return res

        return solve(0, 0)
