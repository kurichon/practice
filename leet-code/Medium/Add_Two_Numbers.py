# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2 = [],[]
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        n1 = int("".join(map(str, num1[::-1])))
        n2 = int("".join(map(str, num2[::-1])))
        sum = n1 + n2

        output_List = ListNode()
        curr = output_List
        for digit in str(sum)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
        return output_List.next
