# 这里有 n 个航班，它们分别从 1 到 n 进行编号。

# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

# 请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。

# class Solution:
#     def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
#         answer=[0]*n
#         for firsti,lasti,seatsi in bookings:
#             for i in range(firsti,lasti+1):
#                 answer[i-1]+=seatsi
#         return answer

class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        answer=[0]*n
        diff=[0]*(n+1)
        for firsti,lasti,seatsi in bookings:
            diff[firsti-1]+=seatsi
            diff[lasti]-=seatsi
        for i in range(n):
            answer[i]=answer[i-1]+diff[i]
        return answer
if __name__ =='__main__':
    s=Solution()
    s.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5)