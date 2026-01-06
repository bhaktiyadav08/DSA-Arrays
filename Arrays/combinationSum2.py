class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, curr, remain):
            if remain == 0:
                result.append(list(curr))
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Prune the recursion
                if candidates[i] > remain:
                    break

                curr.append(candidates[i])
                backtrack(i + 1, curr, remain - candidates[i])
                curr.pop()

        backtrack(0, [], target)
        return result
