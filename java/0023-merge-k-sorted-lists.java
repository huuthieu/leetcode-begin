import java.util.*;

/**
 * LeetCode Problem 0023: Merge K Sorted Lists
 *
 * Problem:
 * You are given an array of k linked-lists lists, each linked-list is sorted
 * in ascending order. Merge all the linked-lists into one sorted linked-list.
 *
 * Examples:
 * 1. Input: lists = [[1,4,5],[1,3,4],[2,6]], Output: [1,1,2,1,3,4,4,5,6]
 * 2. Input: lists = [], Output: []
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public class MergeKSortedLists {

    // Q1: Min-heap approach (optimal)
    public static ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;

        PriorityQueue<ListNode> heap = new PriorityQueue<>((a, b) -> a.val - b.val);

        for (ListNode list : lists) {
            if (list != null) heap.offer(list);
        }

        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (!heap.isEmpty()) {
            ListNode node = heap.poll();
            current.next = node;
            current = current.next;

            if (node.next != null) {
                heap.offer(node.next);
            }
        }

        return dummy.next;
    }

    // Q2: Divide and conquer
    public static ListNode mergeKListsDivideConquer(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        return mergeListsHelper(lists, 0, lists.length - 1);
    }

    private static ListNode mergeListsHelper(ListNode[] lists, int left, int right) {
        if (left == right) return lists[left];
        if (left > right) return null;

        int mid = (left + right) / 2;
        ListNode l1 = mergeListsHelper(lists, left, mid);
        ListNode l2 = mergeListsHelper(lists, mid + 1, right);

        return mergeTwo(l1, l2);
    }

    private static ListNode mergeTwo(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }

        current.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }

    // Q3: Iterative merge
    public static ListNode mergeKListsIterative(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;

        while (lists.length > 1) {
            List<ListNode> newLists = new ArrayList<>();

            for (int i = 0; i < lists.length; i += 2) {
                ListNode merged = (i + 1 < lists.length) ?
                    mergeTwo(lists[i], lists[i + 1]) : lists[i];
                newLists.add(merged);
            }

            lists = newLists.toArray(new ListNode[0]);
        }

        return lists[0];
    }

    public static void main(String[] args) {
        // Test case
        ListNode[] lists = new ListNode[3];
        lists[0] = createList(new int[]{1, 4, 5});
        lists[1] = createList(new int[]{1, 3, 4});
        lists[2] = createList(new int[]{2, 6});

        System.out.println("Q1: mergeKLists (Heap)");
        System.out.println("  Result: " + listToArray(mergeKLists(lists)));
    }

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
}
