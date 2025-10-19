"""
LeetCode Problem 0025: Reverse Nodes in K-Group

Problem:
Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list. k is a positive integer and is less than or
equal to the length of the linked list.

If the number of nodes is not a multiple of k then left-out nodes, in the end,
should remain as is.

Examples:
1. Input: head = [1,2,3,4,5], k = 2, Output: [2,1,4,3,5]
2. Input: head = [1,2,3,4,5], k = 3, Output: [3,2,1,4,5]
3. Input: head = [1,2,3,4,5], k = 1, Output: [1,2,3,4,5]

Constraints:
- The number of nodes in the list is n
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Q1: Iterative approach with helper function (optimal)
def reverseKGroup_iterative(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Reverse k nodes at a time iteratively, linking groups together.
    """
    def get_kth(node, k):
        while node and k > 1:
            node = node.next
            k -= 1
        return node

    def reverse_between(head, tail):
        prev = tail.next
        current = head
        while prev != tail:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return tail, head

    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy

    while True:
        kth = get_kth(prev_group, k + 1)
        if not kth:
            break

        group_start = prev_group.next
        group_end = kth

        next_group = group_end.next
        prev_group.next, group_end.next = reverse_between(group_start, group_end)
        prev_group = group_start

    return dummy.next


# Q2: Recursive approach
def reverseKGroup_recursive(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n/k) for recursion stack

    Approach: Recursively reverse groups of k nodes.
    """
    current = head
    count = 0

    while current and count < k:
        current = current.next
        count += 1

    if count < k:
        return head

    new_head = None
    current = head
    prev = None

    for _ in range(k):
        next_node = current.next
        current.next = new_head
        new_head = current
        current = next_node

    head.next = reverseKGroup_recursive(current, k)
    return new_head


# Q3: Stack-based approach
def reverseKGroup_stack(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(k) for stack

    Approach: Use a stack to reverse k nodes at a time.
    """
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    stack = []

    while True:
        current = prev_group.next
        for _ in range(k):
            if not current:
                return dummy.next
            stack.append(current)
            current = current.next

        while stack:
            prev_group.next = stack.pop()
            prev_group = prev_group.next

        prev_group.next = current

    return dummy.next


# Q4: Reverse sublist helper approach
def reverseKGroup_helper(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach: Use helper function to reverse sublist.
    """
    def reverse_list(node, count):
        if not node or count == 0:
            return node
        prev = None
        current = node
        for _ in range(count):
            if not current:
                break
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def get_length(node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    length = get_length(head)
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    current = head

    while length >= k:
        prev_group.next = reverse_list(current, k)
        new_tail = current
        for _ in range(k):
            current = current.next

        new_tail.next = current
        prev_group = new_tail
        length -= k

    return dummy.next


# Q5: Simplified recursive approach
def reverseKGroup_simple_recursive(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n/k)

    Approach: Simple recursive reversal of k groups.
    """
    node = head
    for _ in range(k):
        if not node:
            return head
        node = node.next

    prev = None
    current = head
    for _ in range(k):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    head.next = reverseKGroup_simple_recursive(current, k)
    return prev


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
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ([1, 2], 2, [2, 1]),
        ([1], 1, [1]),
        ([1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5]),
    ]

    functions = [
        reverseKGroup_iterative,
        reverseKGroup_recursive,
        reverseKGroup_stack,
        reverseKGroup_helper,
        reverseKGroup_simple_recursive,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for values, k, expected in test_cases:
            head = create_linked_list(values)
            result = func(head, k)
            result_list = linked_list_to_list(result)
            passed = result_list == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} reverseKGroup({values}, {k}) = {result_list}")

        if all_passed:
            print(f"  All tests passed!")
