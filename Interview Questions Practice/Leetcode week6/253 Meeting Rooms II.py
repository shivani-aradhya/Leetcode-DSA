class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        p1, p2 = 0, 0
        while p1 < len(intervals):
            if start[p1] < end[p2]:
                p1 += 1
                count += 1
            else:
                p2 += 1
                count -= 1
            res = max(res, count)
        return res