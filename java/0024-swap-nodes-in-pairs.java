/**
 * LeetCode Problem 0024: Swap Nodes in Pairs
 *
 * Problem:
 * Given a linked list, swap every two adjacent nodes and return its head.
 *
 * Examples:
 * 1. Input: head = [1,2,3,4], Output: [2,1,4,3]
 * 2. Input: head = [], Output: []
 * 3. Input: head = [1], Output: [1]
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public class SwapNodesInPairs {

    // Q1: Iterative approach (optimal)
    public static ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            prev.next = second;
            first.next = second.next;
            second.next = first;

            prev = first;
        }

        return dummy.next;
    }

    // Q2: Recursive approach
    public static ListNode swapPairsRecursive(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode first = head;
        ListNode second = head.next;

        first.next = swapPairsRecursive(second.next);
        second.next = first;

        return second;
    }

    // Q3: Three-pointer approach
    public static ListNode swapPairsThreePointer(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode current = dummy;

        while (current.next != null && current.next.next != null) {
            ListNode prev_node = current.next;
            ListNode curr_node = current.next.next;

            prev_node.next = curr_node.next;
            curr_node.next = prev_node;
            current.next = curr_node;
            current = prev_node;
        }

        return dummy.next;
    }

    // Helper methods for testing
    private static ListNode createList(int[] values) {
        if (values.length == 0) return null;
        ListNode head = new ListNode(values[0]);
        ListNode current = head;
        for (int i = 1; i < values.length; i++) {
            current.next = new ListNode(values[i]);
            current = current.next;
        }
        return head;
    }

    private static void printList(ListNode head) {
        System.out.print("[");
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val);
            if (current.next != null) System.out.print(",");
            current = current.next;
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        System.out.println("Q1: swapPairs (Iterative)");
        ListNode head1 = createList(new int[]{1, 2, 3, 4});
        System.out.print("  Result: ");
        printList(swapPairs(head1));

        System.out.println("\nQ2: swapPairs (Recursive)");
        ListNode head2 = createList(new int[]{1, 2, 3, 4});
        System.out.print("  Result: ");
        printList(swapPairsRecursive(head2));
    }
}
