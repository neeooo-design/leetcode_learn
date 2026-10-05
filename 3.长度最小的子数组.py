# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
# 如果不存在符合条件的子数组，返回 0 。class Solution:
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        for sub_len in range(1,len(nums)+1):
            for begin in range(0,len(nums)-sub_len+1):
                total =sum(nums[begin:begin+sub_len])
                if total >= target:
                    return sub_len      
        return 0
            