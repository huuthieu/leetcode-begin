"""
LeetCode Problem 0023: Merge K Sorted Lists

Problem:
You are given an array of k linked-lists lists, each linked-list is sorted
in ascending order. Merge all the linked-lists into one sorted linked-list
and return it.

Examples:
1. Input: lists = [[1,4,5],[1,3,4],[2,6]], Output: [1,1,2,1,3,4,4,5,6]
2. Input: lists = [], Output: []
3. Input: lists = [[]], Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
"""

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Q1: Min-heap approach (optimal)
def mergeKLists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time Complexity: O(n * log k) where n is total number of nodes
    Space Complexity: O(k)

    Approach: Use a min-heap to always merge the smallest element next.
    """
    if not lists:
        return None

    dummy = ListNode(0)
    current = dummy
    heap = []

    # Add first node of each list to heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    while heap:
        val, idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next


# Q2: Divide and conquer approach
def mergeKLists_divide_conquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time Complexity: O(n * log k)
    Space Complexity: O(log k) for recursion stack

    Approach: Recursively divide the lists in half and merge.
    """
    if not lists:
        return None

    def merge_two(l1, l2):
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next

    def merge_lists(left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = merge_lists(left, mid)
        l2 = merge_lists(mid + 1, right)
        return merge_two(l1, l2)

    return merge_lists(0, len(lists) - 1)


# Q3: Iterative merge approach
def mergeKLists_iterative(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time Complexity: O(n * log k)
    Space Complexity: O(1)

    Approach: Iteratively merge lists two at a time.
    """
    if not lists:
        return None

    def merge_two(l1, l2):
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next

    while len(lists) > 1:
        new_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged = merge_two(lists[i], lists[i + 1])
            else:
                merged = lists[i]
            new_lists.append(merged)
        lists = new_lists

    return lists[0]


# Q4: Using priority queue (different heap implementation)
def mergeKLists_pq(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time Complexity: O(n * log k)
    Space Complexity: O(k)

    Approach: Similar to heap but more explicit priority queue handling.
    """
    if not lists or all(not lst for lst in lists):
        return None

    dummy = ListNode(0)
    current = dummy
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    count = 0
    while heap:
        val, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        count += 1

        if node.next:
            heapq.heappush(heap, (node.next.val, count, node.next))

    return dummy.next


# Q5: Recursive merge approach
def mergeKLists_recursive(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time Complexity: O(n * log k)
    Space Complexity: O(log k)

    Approach: Recursively merge pairs of lists.
    """
    if not lists:
        return None

    def merge_two(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = merge_two(l1.next, l2)
            return l1
        else:
            l2.next = merge_two(l1, l2.next)
            return l2

    def merge_lists_helper(left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = merge_lists_helper(left, mid)
        l2 = merge_lists_helper(mid + 1, right)
        return merge_two(l1, l2)

    return merge_lists_helper(0, len(lists) - 1)


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
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 1, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1]], [1]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ]

    functions = [
        mergeKLists_heap,
        mergeKLists_divide_conquer,
        mergeKLists_iterative,
        mergeKLists_pq,
        mergeKLists_recursive,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for lists_vals, expected in test_cases:
            lists = [create_linked_list(vals) for vals in lists_vals]
            result = func(lists)
            result_list = sorted(linked_list_to_list(result))
            expected_sorted = sorted(expected)
            passed = result_list == expected_sorted
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            print(f"  {status} mergeKLists({lists_vals}) = {result_list}")

        if all_passed:
            print(f"  All tests passed!")
