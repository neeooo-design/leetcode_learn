# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

# 整数除法仅保留整数部分。

# 你可以假设给定的表达式总是有效的。所有中间结果将在 [-231, 231 - 1] 的范围内。

# 注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(" ","")
        stack=[]
        n=len(s)
        num=0
        pre_char="+"
        for i in range(n):
            char=s[i]
            if char.isdigit():
                num=num*10+int(char)
            if not char.isdigit() or i==n-1:    
                if pre_char=="+":
                    stack.append(num)
                if pre_char=="-":
                    stack.append(-num)
                if pre_char=="*":
                    top=stack.pop()
                    stack.append(top*num)
                if pre_char=="/":
                    top=stack.pop()
                    stack.append(int(top/num))
                    
                num=0
                pre_char=char
        return sum(stack)