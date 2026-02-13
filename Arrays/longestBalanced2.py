class Solution:
    def longestBalanced(self, s):
        n = len(s)
        ans = 0
        
        # Prefix sums for a, b, c
        a = [0] * (n + 1)
        b = [0] * (n + 1)
        c = [0] * (n + 1)
        
        for i in range(n):
            a[i + 1] = a[i]
            b[i + 1] = b[i]
            c[i + 1] = c[i]
            if s[i] == 'a':
                a[i + 1] += 1
            elif s[i] == 'b':
                b[i + 1] += 1
            else:
                c[i + 1] += 1
        
        # Case 1: Single character substring (all same char)
        curr_char = ''
        curr_len = 0
        for ch in s:
            if ch == curr_char:
                curr_len += 1
            else:
                curr_char = ch
                curr_len = 1
            ans = max(ans, curr_len)
        
        # Case 2: Two distinct characters with equal frequency
        # Check pairs: (a,b), (a,c), (b,c)
        def longest_pair(x, y, z):
            # x, y are the two chars we want to balance, z is the third char to avoid
            count_x = count_y = 0
            diff_map = {0: 0}  # diff -> first index where this diff occurs
            res = 0
            
            for i, ch in enumerate(s):
                if ch == z:  # Reset when we hit the third character
                    diff_map = {0: i + 1}
                    count_x = count_y = 0
                    continue
                
                if ch == x:
                    count_x += 1
                elif ch == y:
                    count_y += 1
                
                diff = count_x - count_y
                if diff in diff_map:
                    res = max(res, i - diff_map[diff] + 1)
                else:
                    diff_map[diff] = i + 1
            
            return res
        
        ans = max(ans, longest_pair('a', 'b', 'c'))
        ans = max(ans, longest_pair('a', 'c', 'b'))
        ans = max(ans, longest_pair('b', 'c', 'a'))
        
        # Case 3: All three characters with equal frequency
        # We need: count_a == count_b == count_c
        # Using: 2*a - b - c as the key (if equal at i and j, then a[i]-a[j] == b[i]-b[j] == c[i]-c[j])
        diff_map = {0: [0]}  # diff -> list of indices
        for i in range(n):
            diff = 2 * a[i + 1] - b[i + 1] - c[i + 1]
            if diff not in diff_map:
                diff_map[diff] = []
            
            # Check all previous indices with same diff
            for idx in diff_map[diff]:
                # Verify that a, b, c counts are actually equal between idx and i+1
                ca = a[i + 1] - a[idx]
                cb = b[i + 1] - b[idx]
                cc = c[i + 1] - c[idx]
                if ca == cb == cc and ca > 0:  # Must have at least one of each
                    ans = max(ans, i - idx + 1)
                    break  # Earlier indices give longer substrings
            
            diff_map[diff].append(i + 1)
        
        return ans