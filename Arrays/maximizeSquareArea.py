class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        hFences += [1, m]
        vFences += [1, n]

        hFences.sort()
        vFences.sort()

        def get_distances(arr):
            distances = set()
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    distances.add(arr[j] - arr[i])
            return distances

        hDistances = get_distances(hFences)
        vDistances = get_distances(vFences)

        common = hDistances & vDistances
        if not common:
            return -1

        max_side = max(common)
        return (max_side * max_side) % MOD
