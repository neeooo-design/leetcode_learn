# 给定一个整数数组  nums，处理以下类型的多个查询:

# 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
# 实现 NumArray 类：

# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，
# 包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )

# class NumArray:

#     def __init__(self, nums: list[int]):
#          self.cache={}
#          for i,item in enumerate(nums):
#               self.cache[i]=item

#     def sumRange(self, left: int, right: int) -> int:
#         sum=0
#         for i in range(left,right+1):
#              sum+=self.cache[i]
#         return sum

class NumArray:

    def __init__(self, nums: list[int]):
         self.nums=nums
         self.sums=[0]*(len(nums)+1)
         self.sums[0]=0
         for i in range(1,len(self.nums)+1):
              self.sums[i]=nums[i-1]+self.sums[i-1]
         print(self.nums)
         print(self.sums)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]
if __name__ == '__main__':
     n=NumArray([0,1,2,3,4])
     print(n.sumRange(2,3))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)