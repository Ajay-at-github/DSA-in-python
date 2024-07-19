# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        NewHead = None  # Initialize NewHead to None
        
        prev = None
        curr = head
        
        while curr and curr.next:
            nextPair = curr.next.next
            temp = curr.next
            
            # Swap
            curr.next = nextPair
            temp.next = curr
            
            if prev:
                prev.next = temp
            else:
                NewHead = temp  # Set NewHead to the first swapped pair
            
            # Move to the next pair
            prev = curr
            curr = nextPair
        
        return NewHead
