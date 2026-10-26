# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
# 
# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         return_list = []
#         for i, item in enumerate(temperatures):
#             stack = []
#             stack.append(item)
#             num = i + 1
#             found = False
#             while num < len(temperatures):
#                 if temperatures[num] <= item:
#                     stack.append(temperatures[num])
#                 else:
#                     return_list.append(len(stack))
#                     found = True
#                     break
#                 num += 1
#             if not found:
#                 return_list.append(0)
#         return return_list
# 单调栈
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        answer=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while True:
                if stack!=[] and temperatures[i] > temperatures[stack[-1]]:
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                else:
                    stack.append(i)
                    break
        return answer