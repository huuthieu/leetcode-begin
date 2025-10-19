"""
LeetCode Problem 0021: Merge Two Sorted Lists

Problem:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the two lists.

Return the head of the merged linked list.

Examples:
1. Input: list1 = [1,2,4], list2 = [1,3,4], Output: [1,1,2,3,4,4]
2. Input: list1 = [], list2 = [], Output: []
3. Input: list1 = [], list2 = [0], Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Q1: Iterative approach (optimal)
def mergeTwoLists_iterative(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n + m)
    Space Complexity: O(1)

    Approach: Create a dummy node and iterate through both lists,
    always appending the smaller value to the merged list.
    """
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach remaining nodes
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


# Q2: Recursive approach
def mergeTwoLists_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n + m)
    Space Complexity: O(n + m) for recursion stack

    Approach: Recursively choose the smaller node and merge the rest.
    """
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists_recursive(list1, list2.next)
        return list2


# Q3: Using helper function
def mergeTwoLists_helper(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n + m)
    Space Complexity: O(1)

    Approach: Use a helper function to manage the merge process.
    """
    def merge_helper(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = merge_helper(l1.next, l2)
            return l1
        else:
            l2.next = merge_helper(l1, l2.next)
            return l2

    return merge_helper(list1, list2)


# Q4: While loop with direct assignment
def mergeTwoLists_while(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n + m)
    Space Complexity: O(1)

    Approach: Simple while loop with direct node assignment.
    """
    if not list1:
        return list2
    if not list2:
        return list1

    head = ListNode(0)
    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return head.next


# Q5: Tail recursion approach
def mergeTwoLists_tail_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n + m)
    Space Complexity: O(n + m) for recursion stack

    Approach: Tail recursion to maintain better readability.
    """
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists_tail_recursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists_tail_recursive(list1, list2.next)
        return list2


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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [], [1]),
        ([2], [1], [1, 2]),
        ([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([5], [1, 2, 3, 4], [1, 2, 3, 4, 5]),
    ]

    functions = [
        mergeTwoLists_iterative,
        mergeTwoLists_recursive,
        mergeTwoLists_helper,
        mergeTwoLists_while,
        mergeTwoLists_tail_recursive,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for list1_vals, list2_vals, expected in test_cases:
            list1 = create_linked_list(list1_vals)
            list2 = create_linked_list(list2_vals)
            result = func(list1, list2)
            result_list = linked_list_to_list(result)
            passed = result_list == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} merge({list1_vals}, {list2_vals}) = {result_list}")

        if all_passed:
            print(f"  All tests passed!")
