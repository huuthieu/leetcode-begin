/**
 * LeetCode 206: Reverse Linked List
 *
 * Problem:
 * Given the head of a singly linked list, reverse the list, and return the reversed list.
 *
 * Example:
 * Input: head = [1,2,3,4,5] => Output: [5,4,3,2,1]
 * Input: head = [1,2] => Output: [2,1]
 * Input: head = [] => Output: []
 */

public class ReverseLinkedList {

    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {}

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    // Approach 1: Iterative Reversal
    public static ListNode reverseList_Iterative(ListNode head) {
        /**
         * Use three pointers: prev, current, next
         * Time: O(n), Space: O(1)
         */
        ListNode prev = null;
        ListNode current = head;

        while (current != null) {
            // Store next node
            ListNode nextTemp = current.next;

            // Reverse the link
            current.next = prev;

            // Move prev and current one step forward
            prev = current;
            current = nextTemp;
        }

        return prev;
    }

    // Approach 2: Recursive Reversal
    public static ListNode reverseList_Recursive(ListNode head) {
        /**
         * Recursively reverse the list
         * Time: O(n), Space: O(n) for recursion stack
         */
        if (head == null || head.next == null) {
            return head;
        }

        // Reverse the rest of the list
        ListNode newHead = reverseList_Recursive(head.next);

        // Put first element at the end
        head.next.next = head;
        head.next = null;

        return newHead;
    }

    // Approach 3: Tail Recursive
    public static ListNode reverseList_TailRecursive(ListNode head) {
        return reverseHelper(head, null);
    }

    private static ListNode reverseHelper(ListNode current, ListNode prev) {
        if (current == null) {
            return prev;
        }

        ListNode nextTemp = current.next;
        current.next = prev;

        return reverseHelper(nextTemp, current);
    }

    // Helper: Create linked list from array
    public static ListNode createLinkedList(int[] values) {
        if (values.length == 0) return null;
        ListNode head = new ListNode(values[0]);
        ListNode current = head;
        for (int i = 1; i < values.length; i++) {
            current.next = new ListNode(values[i]);
            current = current.next;
        }
        return head;
    }

    // Helper: Convert linked list to array
    public static int[] linkedListToArray(ListNode head) {
        java.util.List<Integer> list = new java.util.ArrayList<>();
        ListNode current = head;
        while (current != null) {
            list.add(current.val);
            current = current.next;
        }
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }
        return result;
    }

    // Test Cases
    public static void main(String[] args) {
        int[][] testCases = {
            {1, 2, 3, 4, 5},
            {1, 2},
            {1},
            {},
            {1, 2, 3}
        };

        int[][] expectedResults = {
            {5, 4, 3, 2, 1},
            {2, 1},
            {1},
            {},
            {3, 2, 1}
        };

        for (int i = 0; i < testCases.length; i++) {
            int[] inputArray = testCases[i];
            int[] expected = expectedResults[i];

            // Test iterative
            ListNode head1 = createLinkedList(inputArray);
            int[] result1 = linkedListToArray(reverseList_Iterative(head1));

            // Test recursive
            ListNode head2 = createLinkedList(inputArray);
            int[] result2 = linkedListToArray(reverseList_Recursive(head2));

            // Test tail recursive
            ListNode head3 = createLinkedList(inputArray);
            int[] result3 = linkedListToArray(reverseList_TailRecursive(head3));

            assert java.util.Arrays.equals(result1, expected) : "Iterative failed";
            assert java.util.Arrays.equals(result2, expected) : "Recursive failed";
            assert java.util.Arrays.equals(result3, expected) : "TailRecursive failed";

            System.out.println("Test case " + i + ": ✓");
        }

        System.out.println("\nAll tests passed!");
    }
}
