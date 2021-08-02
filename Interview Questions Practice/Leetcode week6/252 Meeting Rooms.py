class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        endtime =-1
        for start, end in intervals:
            if endtime <= start:
                endtime = end
            else:
                return False
        return True