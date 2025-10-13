/**
 * 2. Add Two Numbers
 *
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order, and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 *
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 *
 * Example 1:
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 *
 * Example 2:
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 *
 * Example 3:
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 *
 * Constraints:
 * - The number of nodes in each linked list is in the range [1, 100].
 * - 0 <= Node.val <= 9
 * - It is guaranteed that the list represents a number that does not have leading zeros.
 */

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    /**
     * Approach: Simulate digit-by-digit addition with carry
     *
     * Time Complexity: O(max(m, n)) where m and n are the lengths of l1 and l2
     * Space Complexity: O(max(m, n)) for the result linked list
     *
     * Algorithm:
     * 1. Create a dummy head node to simplify result list construction
     * 2. Iterate through both lists simultaneously
     * 3. For each position, add the corresponding digits plus any carry from previous position
     * 4. Create a new node with the digit (sum % 10) and update carry (sum / 10)
     * 5. Continue until both lists are exhausted and carry is 0
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0;

        // Process both lists until exhausted
        while (l1 != null || l2 != null || carry != 0) {
            // Get current digit values (0 if list is exhausted)
            int val1 = (l1 != null) ? l1.val : 0;
            int val2 = (l2 != null) ? l2.val : 0;

            // Calculate sum and new carry
            int sum = val1 + val2 + carry;
            carry = sum / 10;
            int digit = sum % 10;

            // Create new node with the digit
            current.next = new ListNode(digit);
            current = current.next;

            // Move to next nodes if available
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        return dummyHead.next;
    }

    /**
     * Alternative approach: Recursive solution
     *
     * Time Complexity: O(max(m, n))
     * Space Complexity: O(max(m, n)) due to recursion stack
     */
    public ListNode addTwoNumbersRecursive(ListNode l1, ListNode l2) {
        return addTwoNumbersHelper(l1, l2, 0);
    }

    private ListNode addTwoNumbersHelper(ListNode l1, ListNode l2, int carry) {
        // Base case: both lists exhausted and no carry
        if (l1 == null && l2 == null && carry == 0) {
            return null;
        }

        // Get current values
        int val1 = (l1 != null) ? l1.val : 0;
        int val2 = (l2 != null) ? l2.val : 0;

        // Calculate sum
        int sum = val1 + val2 + carry;
        int digit = sum % 10;
        int newCarry = sum / 10;

        // Create current node
        ListNode result = new ListNode(digit);

        // Recursively process next nodes
        ListNode next1 = (l1 != null) ? l1.next : null;
        ListNode next2 = (l2 != null) ? l2.next : null;
        result.next = addTwoNumbersHelper(next1, next2, newCarry);

        return result;
    }
}
