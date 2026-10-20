# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 遍历新建链表
# class Solution:
#     def reverseList(self, head: ListNode | None) -> ListNode | None:
#         new_next=None
#         while head!=None:
#             new_node=ListNode(head.val,new_next)
#             new_next=new_node
#             head=head.next

#         return new_next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head==None:
            return None
        next=head.next
        pre=None
        while head!=None:
            head.next=pre
            pre=head
            head=next
            if head!=None:
                next=head.next
        return pre