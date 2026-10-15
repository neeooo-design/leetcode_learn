# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        i=0
        ret=[]
        left=intervals[0]
        while i<(len(intervals)-1):
            right=intervals[i+1]
            if left[1]>=right[0]:
                left[1]=max(left[1],right[1])
            else:
                ret.append(left)
                left=right
            i+=1
        ret.append(left)
        
        return ret

if __name__ =='__main__':
    s=Solution()
    s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]])