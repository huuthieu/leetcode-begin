/**
 * LeetCode Problem 0025: Reverse Nodes in K-Group
 *
 * Problem:
 * Given the head of a linked list, reverse the nodes of the list k at a time,
 * and return the modified list.
 *
 * Examples:
 * 1. Input: head = [1,2,3,4,5], k = 2, Output: [2,1,4,3,5]
 * 2. Input: head = [1,2,3,4,5], k = 3, Output: [3,2,1,4,5]
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public class ReverseNodesInKGroup {

    // Q1: Iterative approach (optimal)
    public static ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevGroup = dummy;

        while (true) {
            ListNode kth = getKth(prevGroup, k + 1);
            if (kth == null) break;

            ListNode groupStart = prevGroup.next;
            ListNode groupEnd = kth;
            ListNode nextGroup = groupEnd.next;

            ListNode[] reversed = reverseList(groupStart, groupEnd);
            prevGroup.next = reversed[0];
            reversed[1].next = nextGroup;
            prevGroup = reversed[1];
        }

        return dummy.next;
    }

    private static ListNode getKth(ListNode node, int k) {
        while (node != null && k > 1) {
            node = node.next;
            k--;
        }
        return node;
    }

    private static ListNode[] reverseList(ListNode head, ListNode tail) {
        ListNode prev = tail.next;
        ListNode current = head;

        while (prev != tail) {
            ListNode nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }

        return new ListNode[]{tail, head};
    }

    // Q2: Recursive approach
    public static ListNode reverseKGroupRecursive(ListNode head, int k) {
        ListNode current = head;
        int count = 0;

        while (current != null && count < k) {
            current = current.next;
            count++;
        }

        if (count < k) return head;

        ListNode newHead = null;
        current = head;
        ListNode prev = null;

        for (int i = 0; i < k; i++) {
            ListNode nextNode = current.next;
            current.next = newHead;
            newHead = current;
            current = nextNode;
        }

        head.next = reverseKGroupRecursive(current, k);
        return newHead;
    }

    // Q3: With length check
    public static ListNode reverseKGroupWithLength(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevGroup = dummy;
        ListNode current = head;

        int length = 0;
        ListNode temp = head;
        while (temp != null) {
            length++;
            temp = temp.next;
        }

        while (length >= k) {
            ListNode groupStart = current;
            ListNode prev = prevGroup;

            for (int i = 0; i < k; i++) {
                ListNode nextNode = current.next;
                current.next = prev;
                prev = current;
                current = nextNode;
            }

            ListNode temp2 = prevGroup.next;
            prevGroup.next = prev;
            prevGroup = temp2;
            length -= k;
        }

        return dummy.next;
    }

    // Helper methods
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
        System.out.println("Q1: reverseKGroup (Iterative)");
        ListNode head1 = createList(new int[]{1, 2, 3, 4, 5});
        System.out.print("  Result: ");
        printList(reverseKGroup(head1, 2));

        System.out.println("\nQ2: reverseKGroup (Recursive)");
        ListNode head2 = createList(new int[]{1, 2, 3, 4, 5});
        System.out.print("  Result: ");
        printList(reverseKGroupRecursive(head2, 2));
    }
}
