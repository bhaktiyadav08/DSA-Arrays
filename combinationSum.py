class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, curr, total):
            if total == target:
                result.append(list(curr))   # FIXED
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, total + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return result
