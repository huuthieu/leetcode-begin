import java.util.*;

/**
 * LeetCode Problem 0021: Merge Two Sorted Lists
 *
 * Problem:
 * You are given the heads of two sorted linked lists list1 and list2.
 * Merge the two lists in a one sorted list. The list should be made by splicing
 * together the nodes of the two lists.
 *
 * Examples:
 * 1. Input: list1 = [1,2,4], list2 = [1,3,4], Output: [1,1,2,3,4,4]
 * 2. Input: list1 = [], list2 = [], Output: []
 * 3. Input: list1 = [], list2 = [0], Output: [0]
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public class MergeTwoSortedLists {

    // Q1: Iterative approach (optimal)
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        current.next = (list1 != null) ? list1 : list2;
        return dummy.next;
    }

    // Q2: Recursive approach
    public static ListNode mergeTwoListsRecursive(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;

        if (list1.val <= list2.val) {
            list1.next = mergeTwoListsRecursive(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoListsRecursive(list1, list2.next);
            return list2;
        }
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

    private static List<Integer> listToArray(ListNode head) {
        List<Integer> result = new ArrayList<>();
        ListNode current = head;
        while (current != null) {
            result.add(current.val);
            current = current.next;
        }
        return result;
    }

    public static void main(String[] args) {
        int[][] testCases1 = {{1, 2, 4}, {1, 3, 4}};
        int[][] testCases2 = {{}, {}};
        int[][] testCases3 = {{}, {0}};

        System.out.println("Q1: mergeTwoLists (Iterative)");
        ListNode list1 = createList(testCases1[0]);
        ListNode list2 = createList(testCases1[1]);
        System.out.println("  Result: " + listToArray(mergeTwoLists(list1, list2)));
    }
}
