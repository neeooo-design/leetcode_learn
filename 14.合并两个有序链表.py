# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
#         if not list1: return list2
#         if not list2: return list1
#         if list1.val<=list2.val:
#             begin=list1
#             list1=list1.next
#         else:
#             begin=list2
#             list2=list2.next
#         new_list=begin
#         while list1!=None and list2!=None:
#             if list1.val<=list2.val:
#                 new_list.next=list1
#                 list1=list1.next
#             else:
#                 new_list.next=list2
#                 list2=list2.next
#             new_list=new_list.next
#         if list1!=None:
#             new_list.next=list1
#             list1=list1.next
#             new_list=new_list.next
#         else:
#             new_list.next=list2
#             list2=list2.next
#             new_list=new_list.next
#         return begin
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        current=dummy
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                current.next=list1
                current=current.next
                list1=list1.next
            else:
                current.next=list2
                current=current.next
                list2=list2.next
        if list1== None:
            current.next=list2
        else:
            current.next=list1

        return dummy.next