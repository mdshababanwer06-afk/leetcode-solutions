class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def to_day(date):
            month , day = map(int, date.split("-"))
            days = [31,28,31,30,31,30,31,31,30,31,30,31]

            return sum(days[:month - 1]) + day


        a_start = to_day(arriveAlice)
        a_end = to_day(leaveAlice)
        b_start = to_day(arriveBob)
        b_end = to_day(leaveBob)


        start = max(a_start, b_start)
        end = min(a_end, b_end)

        return max(0, end - start + 1)