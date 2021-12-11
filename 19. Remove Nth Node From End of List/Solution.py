class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        pre = dummy
        fast = head
        count = 0
        while fast.next:
            fast = fast.next
            if count >= n-1: pre = pre.next
            count += 1
        pre.next = pre.next.next
        return dummy.next
