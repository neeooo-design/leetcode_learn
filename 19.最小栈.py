# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 实现 MinStack 类:
# MinStack() 初始化堆栈对象。
# void push(int value) 将元素 value 推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
class MinStack:

    def __init__(self):
        self.num_stack=[]
        self.min_stack=[]

    def push(self, value: int) -> None:
        if self.min_stack==[]:
            self.num_stack.append(value)
            self.min_stack.append(value)
        else:
            self.num_stack.append(value)
            if value<=self.min_stack[-1]:
                self.min_stack.append(value)
            else:
                self.min_stack.append(self.min_stack[-1])
        

    def pop(self) -> None:
        self.num_stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.num_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()