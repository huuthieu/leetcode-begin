"""
LeetCode 206: Reverse Linked List

Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Time Complexity: O(n)
Space Complexity: O(1) for iterative, O(n) for recursive (call stack)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach 1: Iterative Reversal
def reverseList_Iterative(head):
    """
    Use three pointers: prev, current, next
    Reverse the links as we iterate through the list
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head

    while current:
        # Store next node
        next_temp = current.next

        # Reverse the link
        current.next = prev

        # Move prev and current one step forward
        prev = current
        current = next_temp

    return prev


# Approach 2: Recursive Reversal
def reverseList_Recursive(head):
    """
    Recursively reverse the list
    Base case: if head is None or head.next is None, return head
    Recursive case: reverse the tail and connect back
    Time: O(n), Space: O(n) for recursion stack
    """
    if not head or not head.next:
        return head

    # Reverse the rest of the list
    new_head = reverseList_Recursive(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    return new_head


# Approach 3: Stack-based
def reverseList_Stack(head):
    """
    Push all nodes onto a stack, then pop and reconstruct
    Time: O(n), Space: O(n)
    """
    if not head:
        return None

    stack = []
    current = head

    # Push all nodes onto stack
    while current:
        stack.append(current)
        current = current.next

    # Pop and reconstruct
    new_head = stack.pop()
    current = new_head

    while stack:
        current.next = stack.pop()
        current = current.next

    current.next = None
    return new_head


# Helper function to create linked list from list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test Cases
def test_reverseList():
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3], [3, 2, 1]),
    ]

    for input_list, expected in test_cases:
        # Test iterative
        head1 = create_linked_list(input_list)
        result1 = linked_list_to_list(reverseList_Iterative(head1))

        # Test recursive
        head2 = create_linked_list(input_list)
        result2 = linked_list_to_list(reverseList_Recursive(head2))

        # Test stack-based
        head3 = create_linked_list(input_list)
        result3 = linked_list_to_list(reverseList_Stack(head3))

        assert (
            result1 == expected
        ), f"Iterative failed: got {result1}, expected {expected}"
        assert (
            result2 == expected
        ), f"Recursive failed: got {result2}, expected {expected}"
        assert (
            result3 == expected
        ), f"Stack failed: got {result3}, expected {expected}"

        print(f"Input: {input_list} => Output: {expected} ✓")


if __name__ == "__main__":
    test_reverseList()
    print("\nAll tests passed!")
