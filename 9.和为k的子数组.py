# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

# 子数组是数组中元素的连续非空序列。
from typing import List

# 滑动窗口（不使用非递增递减数组）
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         fast=0
#         slow=0
#         my_num=0
#         return_num=0
#         while fast<len(nums):
#             my_num+=nums[fast]
#             fast+=1
#             while my_num>=k and slow<len(nums):
#                 if my_num==k:
#                     return_num+=1
#                 my_num-=nums[slow]
#                 slow+=1
                
#         return return_num

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prenums=[0]*(len(nums)+1)
        for i in range(len(nums)):
            prenums[i+1]=prenums[i]+nums[i]
        print(nums)
        print(prenums)
        return_num=0

        cache={}
        for i,item in enumerate(prenums):
            other=item-k
            if other in cache:
                return_num+=cache[other]
            cache[item]=cache.get(item,0)+1
        return return_num
if __name__ =='__main__':
    s=Solution()
    print(s.subarraySum([1,1,1,1],2))
            
