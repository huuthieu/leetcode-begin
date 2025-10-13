"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Approach: Simulate digit-by-digit addition with carry

    Time Complexity: O(max(m, n)) where m and n are the lengths of l1 and l2
    Space Complexity: O(max(m, n)) for the result linked list

    Algorithm:
    1. Create a dummy head node to simplify result list construction
    2. Iterate through both lists simultaneously
    3. For each position, add the corresponding digits plus any carry from previous position
    4. Create a new node with the digit (sum % 10) and update carry (sum // 10)
    5. Continue until both lists are exhausted and carry is 0
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Process both lists until exhausted
        while l1 or l2 or carry:
            # Get current digit values (0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

    def addTwoNumbersRecursive(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Alternative approach: Recursive solution

        Time Complexity: O(max(m, n))
        Space Complexity: O(max(m, n)) due to recursion stack
        """
        return self._add_helper(l1, l2, 0)

    def _add_helper(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        # Base case: both lists exhausted and no carry
        if not l1 and not l2 and carry == 0:
            return None

        # Get current values
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum
        total = val1 + val2 + carry
        digit = total % 10
        new_carry = total // 10

        # Create current node
        result = ListNode(digit)

        # Recursively process next nodes
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        result.next = self._add_helper(next1, next2, new_carry)

        return result


# Helper function to create linked list from list
def create_linked_list(values):
    """Create a linked list from a list of values"""
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
    """Convert linked list to a list of values"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: 342 + 465 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 1: {linked_list_to_list(result)}")  # Expected: [7, 0, 8]

    # Test case 2: 0 + 0 = 0
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 2: {linked_list_to_list(result)}")  # Expected: [0]

    # Test case 3: 9999999 + 9999 = 10009998
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 3: {linked_list_to_list(result)}")  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]

    # Test recursive approach
    print("\nTesting recursive approach:")
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbersRecursive(l1, l2)
    print(f"Recursive Test: {linked_list_to_list(result)}")  # Expected: [7, 0, 8]
