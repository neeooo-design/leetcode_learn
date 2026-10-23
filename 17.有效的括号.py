# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cache={"(":")","[":"]","{":"}"}
        for i in s:
            if i in {"(","[","{"}:
                stack.append(i)
            else:
                if stack==[]:
                    return False
                top_s=stack.pop()
                if i!=cache[top_s]:
                    return False
        if stack!=[]:
            return False
        return True