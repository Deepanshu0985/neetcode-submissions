class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1️⃣ Find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None   # split

        # 2️⃣ Reverse second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev = head of reversed list

        # 3️⃣ Merge both halves
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2