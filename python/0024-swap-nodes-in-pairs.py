"""
LeetCode Problem 0024: Swap Nodes in Pairs

Problem:
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed).

Examples:
1. Input: head = [1,2,3,4], Output: [2,1,4,3]
2. Input: head = [], Output: []
3. Input: head = [1], Output: [1]

Constraints:
- The number of nodes in the list is in the range [0, 100]
- 0 <= Node.val <= 100
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Q1: Iterative approach (optimal)
def swapPairs_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use a dummy node and iterate through pairs, swapping pointers.
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first

    return dummy.next


# Q2: Recursive approach
def swapPairs_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) for recursion stack

    Approach: Recursively swap pairs by advancing two nodes at a time.
    """
    if not head or not head.next:
        return head

    first = head
    second = head.next

    first.next = swapPairs_recursive(second.next)
    second.next = first

    return second


# Q3: Iterative with list node tracking
def swapPairs_tracking(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Keep track of previous, first, and second nodes.
    """
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        third = second.next

        second.next = first
        first.next = third
        prev.next = second
        prev = first

    return dummy.next


# Q4: Stack-based approach
def swapPairs_stack(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) for stack

    Approach: Use a stack to manage node swapping.
    """
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    stack = []

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        stack.append(second)
        stack.append(first)

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first

    return dummy.next


# Q5: Recursive with variable assignment
def swapPairs_recursive_var(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) for recursion stack

    Approach: Recursive approach with explicit variable assignment.
    """
    def swap_helper(node):
        if not node or not node.next:
            return node

        next_node = node.next
        remaining = next_node.next
        node.next = swap_helper(remaining)
        next_node.next = node

        return next_node

    return swap_helper(head)


# Q6: Three-pointer approach
def swapPairs_three_pointer(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Maintain three pointers and swap pairs.
    """
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        prev_node = current.next
        curr_node = current.next.next

        prev_node.next = curr_node.next
        curr_node.next = prev_node
        current.next = curr_node
        current = prev_node

    return dummy.next


# Q7: Inline swap without temporary variable
def swapPairs_inline(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Inline swapping without explicit temporary variable.
    """
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        (current.next, current.next.next.next, current.next.next) = (
            current.next.next,
            current.next,
            current.next.next.next,
        )
        current = current.next.next

    return dummy.next


# Helper functions for testing
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
    ]

    functions = [
        swapPairs_iterative,
        swapPairs_recursive,
        swapPairs_tracking,
        swapPairs_stack,
        swapPairs_recursive_var,
        swapPairs_three_pointer,
        swapPairs_inline,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for values, expected in test_cases:
            head = create_linked_list(values)
            result = func(head)
            result_list = linked_list_to_list(result)
            passed = result_list == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} swapPairs({values}) = {result_list}")

        if all_passed:
            print(f"  All tests passed!")
