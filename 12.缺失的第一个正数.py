# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

# class Solution:
#     def firstMissingPositive(self, nums: list[int]) -> int:
#         i=0
#         while True:
#             if i+1 in nums:
#                 i+=1
#             else:
#                 return i+1

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i=0
        while i<len(nums):
            if nums[i]==i+1:
                i+=1
            else:
                if 0<nums[i]<len(nums) and nums[i]!=nums[nums[i]-1]:
                    target=nums[i]
                    target_id=nums[i]-1
                    nums[i]=nums[nums[i]-1]
                    nums[target_id]=target
                else:
                    i+=1
        for i in range(0,len(nums)):
            if i+1==nums[i]:
                pass
            else:
                return i+1
        return len(nums)+1
if __name__ == '__main__':
    s=Solution()
    print(s.firstMissingPositive([1,1]))
                
