"""
LeetCode Problem 0019: Remove Nth Node From End of List

Problem:
Given the head of a linked list, remove the nth node from the end of the list
and return the head of the list.

Examples:
1. Input: head = [1,2,3,4,5], n = 2, Output: [1,2,3,5]
2. Input: head = [1], n = 1, Output: []
3. Input: head = [1,2], n = 1, Output: [1]
4. Input: head = [1,2], n = 2, Output: [2]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Q1: Two-pointer approach (optimal)
def removeNthFromEnd_twopointer(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L) where L is length of list
    Space Complexity: O(1)

    Approach: Use two pointers with gap of n between them. When fast pointer
    reaches end, slow pointer is at the node before the one to be removed.
    """
    # Create a dummy node to handle edge case of removing head
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        if fast is None:
            return head
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # Remove the nth node
    slow.next = slow.next.next

    return dummy.next


# Q2: Count length first approach
def removeNthFromEnd_count_first(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L) - two passes through the list
    Space Complexity: O(1)

    Approach: First pass counts total length, second pass removes the node.
    """
    # Count the length
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next

    # If removing the head
    if length == n:
        return head.next

    # Find the node before the one to remove
    current = head
    for _ in range(length - n - 1):
        current = current.next

    current.next = current.next.next
    return head


# Q3: Recursive approach
def removeNthFromEnd_recursive(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L)
    Space Complexity: O(L) for recursion stack

    Approach: Use recursion to traverse and track position from end.
    """
    position = [0]

    def helper(node):
        if node is None:
            return None

        node.next = helper(node.next)
        position[0] += 1

        if position[0] == n:
            return node.next

        return node

    return helper(head)


# Q4: Stack-based approach
def removeNthFromEnd_stack(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L)
    Space Complexity: O(L)

    Approach: Push all nodes onto stack, then pop to find nth node.
    """
    stack = []
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    # Push all nodes onto stack
    while current is not None:
        stack.append(current)
        current = current.next

    # Pop n times to find the node before the one to remove
    for _ in range(n):
        stack.pop()

    prev = stack[-1]
    prev.next = prev.next.next

    return dummy.next


# Q5: Using list for nodes
def removeNthFromEnd_list(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L)
    Space Complexity: O(L)

    Approach: Store all nodes in a list, then remove by index.
    """
    nodes = []
    current = head

    # Collect all nodes
    while current is not None:
        nodes.append(current)
        current = current.next

    # If removing the head
    if len(nodes) == n:
        return head.next

    # Remove the nth node from end
    nodes[-n].next = nodes[-n].next.next if -n < -len(nodes) else None

    return head


# Q6: Simplified two-pointer
def removeNthFromEnd_simplified(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L)
    Space Complexity: O(1)

    Approach: Two-pointer with dummy node.
    """
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer n+1 steps
    for i in range(n + 1):
        if first is None:
            return head
        first = first.next

    # Move both pointers
    while first is not None:
        first = first.next
        second = second.next

    # Remove node
    second.next = second.next.next

    return dummy.next


# Q7: Using dictionary to track positions
def removeNthFromEnd_dict(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L)
    Space Complexity: O(L)

    Approach: Use dictionary to map nodes to positions.
    """
    nodes = {}
    positions = {}
    current = head
    pos = 0

    # Map nodes and their positions
    while current is not None:
        nodes[pos] = current
        positions[current] = pos
        current = current.next
        pos += 1

    total = pos
    remove_pos = total - n

    # If removing the head
    if remove_pos == 0:
        return head.next

    # Find the node before the one to remove
    prev_node = nodes[remove_pos - 1]
    prev_node.next = prev_node.next.next

    return head


# Q8: Two-pointer with explicit tracking
def removeNthFromEnd_explicit(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L)
    Space Complexity: O(1)

    Approach: Two pointers with explicit distance tracking.
    """
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    # Create gap of n nodes
    for i in range(n):
        if fast.next is None:
            return dummy.next
        fast = fast.next

    # Move until fast reaches the end
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Remove the node
    slow.next = slow.next.next

    return dummy.next


# Q9: With helper function
def removeNthFromEnd_helper(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L)
    Space Complexity: O(1)

    Approach: Helper function for clarity.
    """
    def get_length(node):
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    length = get_length(head)

    if length == n:
        return head.next

    current = head
    for _ in range(length - n - 1):
        current = current.next

    current.next = current.next.next
    return head


# Q10: Clean and simple
def removeNthFromEnd_clean(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time Complexity: O(L)
    Space Complexity: O(1)

    Approach: Clean implementation with dummy node.
    """
    dummy = ListNode(0, head)
    left = dummy
    right = dummy

    # Move right pointer n+1 steps
    for _ in range(n + 1):
        if right is None:
            return head
        right = right.next

    # Move both pointers until right is None
    while right is not None:
        right = right.next
        left = left.next

    # Remove the node
    left.next = left.next.next

    return dummy.next


def list_to_linked_list(arr):
    """Convert list to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Convert linked list to list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
        ([1], 1, []),
        ([2, 1], 2, [1]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ]

    functions = [
        removeNthFromEnd_twopointer,
        removeNthFromEnd_count_first,
        removeNthFromEnd_recursive,
        removeNthFromEnd_stack,
        removeNthFromEnd_list,
        removeNthFromEnd_simplified,
        removeNthFromEnd_dict,
        removeNthFromEnd_explicit,
        removeNthFromEnd_helper,
        removeNthFromEnd_clean,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for arr, n, expected in test_cases:
            head = list_to_linked_list(arr)
            result = func(head, n)
            result_list = linked_list_to_list(result)
            passed = result_list == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} removeNthFromEnd({arr}, {n}) = {result_list} (expected: {expected})")

        if all_passed:
            print(f"  All tests passed!")
