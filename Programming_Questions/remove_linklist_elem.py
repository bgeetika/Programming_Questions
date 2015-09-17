class Solution(object):
    def removeElements(self, head, val):
        new_head = head
        if head is None:
            return head
        prev = head
        while head is not None:
            if head.val == val:
                if new_head == head:
                    new_head = head.next
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return new_head
