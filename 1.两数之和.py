# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n=len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
#         return [] 

#哈希表
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         cache={}
#         for i,item in enumerate(nums):
#             cache[item]=i
#         for i,item in enumerate(nums):
#             other=target-item
#             if other in cache and cache[other]!=i:
#                 return [i,cache[other]]

#哈希表更进一步
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache={}
        for i,item in enumerate(nums):
            other=target-item
            if other in cache:
                return[i,cache[other]]
            cache[item]=i