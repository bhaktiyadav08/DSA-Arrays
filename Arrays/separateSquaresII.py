class Solution:
    def separateSquares(self, squares):
        events = []
        for x, y, s in squares:
            events.append((y, 1, x, x + s))
            events.append((y + s, -1, x, x + s))

        events.sort()
        from bisect import insort, bisect_left

        active = []
        prev_y = events[0][0]
        total_area = 0.0
        slabs = []

        def union_length(intervals):
            total = 0
            cur_s, cur_e = intervals[0]
            for s, e in intervals[1:]:
                if s > cur_e:
                    total += cur_e - cur_s
                    cur_s, cur_e = s, e
                else:
                    cur_e = max(cur_e, e)
            total += cur_e - cur_s
            return total

        i = 0
        while i < len(events):
            y = events[i][0]

            if active and y > prev_y:
                width = union_length(active)
                area = width * (y - prev_y)
                slabs.append((prev_y, y, width))
                total_area += area

            # process all events at this y
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                if typ == 1:
                    insort(active, (x1, x2))
                else:
                    active.pop(bisect_left(active, (x1, x2)))
                i += 1

            prev_y = y

        half = total_area / 2.0
        cur = 0.0

        for a, b, w in slabs:
            area = (b - a) * w
            if cur + area >= half:
                return a + (half - cur) / w
            cur += area

        return 0.0
