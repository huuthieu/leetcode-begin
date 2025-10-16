import java.util.*;

/**
 * LeetCode Problem 0019: Remove Nth Node From End of List
 *
 * Problem:
 * Given the head of a linked list, remove the nth node from the end of the list
 * and return the head of the list.
 *
 * Examples:
 * 1. Input: head = [1,2,3,4,5], n = 2, Output: [1,2,3,5]
 * 2. Input: head = [1], n = 1, Output: []
 */
public class RemoveNthNodeFromEnd {

    static class ListNode {
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

    /**
     * Q1: Two-pointer approach (optimal)
     *
     * Time Complexity: O(L)
     * Space Complexity: O(1)
     */
    public static ListNode removeNthFromEndTwoPointer(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode first = dummy;
        ListNode second = dummy;

        // Move first pointer n+1 steps ahead
        for (int i = 0; i <= n; i++) {
            if (first == null) return head;
            first = first.next;
        }

        // Move both pointers until first reaches null
        while (first != null) {
            first = first.next;
            second = second.next;
        }

        // Remove the node
        second.next = second.next.next;

        return dummy.next;
    }

    /**
     * Q2: Count length first approach
     *
     * Time Complexity: O(L)
     * Space Complexity: O(1)
     */
    public static ListNode removeNthFromEndCountFirst(ListNode head, int n) {
        // Count the length
        int length = 0;
        ListNode current = head;
        while (current != null) {
            length++;
            current = current.next;
        }

        // If removing the head
        if (length == n) {
            return head.next;
        }

        // Find the node before the one to remove
        current = head;
        for (int i = 0; i < length - n - 1; i++) {
            current = current.next;
        }

        current.next = current.next.next;
        return head;
    }

    /**
     * Q3: Stack-based approach
     *
     * Time Complexity: O(L)
     * Space Complexity: O(L)
     */
    public static ListNode removeNthFromEndStack(ListNode head, int n) {
        Stack<ListNode> stack = new Stack<>();
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode current = dummy;

        // Push all nodes onto stack
        while (current != null) {
            stack.push(current);
            current = current.next;
        }

        // Pop n times to find the node before the one to remove
        for (int i = 0; i < n; i++) {
            stack.pop();
        }

        ListNode prev = stack.peek();
        prev.next = prev.next.next;

        return dummy.next;
    }

    /**
     * Q4: Using List to store nodes
     *
     * Time Complexity: O(L)
     * Space Complexity: O(L)
     */
    public static ListNode removeNthFromEndList(ListNode head, int n) {
        List<ListNode> nodes = new ArrayList<>();
        ListNode current = head;

        // Collect all nodes
        while (current != null) {
            nodes.add(current);
            current = current.next;
        }

        // If removing the head
        if (nodes.size() == n) {
            return head.next;
        }

        // Remove the nth node from end
        ListNode prevNode = nodes.get(nodes.size() - n - 1);
        prevNode.next = prevNode.next.next;

        return head;
    }

    /**
     * Q5: Simplified two-pointer
     *
     * Time Complexity: O(L)
     * Space Complexity: O(1)
     */
    public static ListNode removeNthFromEndSimplified(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode first = dummy;
        ListNode second = dummy;

        // Move first pointer n+1 steps
        for (int i = 0; i <= n; i++) {
            if (first == null) return head;
            first = first.next;
        }

        // Move both pointers
        while (first != null) {
            first = first.next;
            second = second.next;
        }

        // Remove node
        second.next = second.next.next;

        return dummy.next;
    }

    /**
     * Q6: Two-pointer with explicit distance
     *
     * Time Complexity: O(L)
     * Space Complexity: O(1)
     */
    public static ListNode removeNthFromEndExplicit(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy;
        ListNode fast = dummy;

        // Create gap of n nodes
        for (int i = 0; i < n; i++) {
            if (fast.next == null) return dummy.next;
            fast = fast.next;
        }

        // Move until fast reaches the end
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }

        // Remove the node
        slow.next = slow.next.next;

        return dummy.next;
    }

    /**
     * Q7: With helper method for length
     *
     * Time Complexity: O(L)
     * Space Complexity: O(1)
     */
    public static ListNode removeNthFromEndHelper(ListNode head, int n) {
        int length = getLength(head);

        if (length == n) {
            return head.next;
        }

        ListNode current = head;
        for (int i = 0; i < length - n - 1; i++) {
            current = current.next;
        }

        current.next = current.next.next;
        return head;
    }

    private static int getLength(ListNode node) {
        int length = 0;
        while (node != null) {
            length++;
            node = node.next;
        }
        return length;
    }

    /**
     * Q8: Using HashMap for position tracking
     *
     * Time Complexity: O(L)
     * Space Complexity: O(L)
     */
    public static ListNode removeNthFromEndHashMap(ListNode head, int n) {
        Map<Integer, ListNode> positionMap = new HashMap<>();
        ListNode current = head;
        int pos = 0;

        // Map positions to nodes
        while (current != null) {
            positionMap.put(pos, current);
            current = current.next;
            pos++;
        }

        int totalLength = pos;
        int removePos = totalLength - n;

        if (removePos == 0) {
            return head.next;
        }

        ListNode prevNode = positionMap.get(removePos - 1);
        prevNode.next = prevNode.next.next;

        return head;
    }

    /**
     * Q9: Recursive approach
     *
     * Time Complexity: O(L)
     * Space Complexity: O(L)
     */
    public static ListNode removeNthFromEndRecursive(ListNode head, int n) {
        int[] pos = {0};

        ListNode helper(ListNode node) {
            if (node == null) return null;

            node.next = helper(node.next);
            pos[0]++;

            if (pos[0] == n) {
                return node.next;
            }

            return node;
        }

        return helper(head);
    }

    /**
     * Q10: Clean and optimal implementation
     *
     * Time Complexity: O(L)
     * Space Complexity: O(1)
     */
    public static ListNode removeNthFromEndClean(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode left = dummy;
        ListNode right = dummy;

        // Move right pointer n+1 steps
        for (int i = 0; i <= n; i++) {
            if (right == null) return head;
            right = right.next;
        }

        // Move both pointers until right is null
        while (right != null) {
            right = right.next;
            left = left.next;
        }

        // Remove the node
        left.next = left.next.next;

        return dummy.next;
    }

    // Utility functions for testing
    private static ListNode arrayToLinkedList(int[] arr) {
        if (arr.length == 0) return null;
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        for (int i = 1; i < arr.length; i++) {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
        return head;
    }

    private static List<Integer> linkedListToArray(ListNode head) {
        List<Integer> result = new ArrayList<>();
        while (head != null) {
            result.add(head.val);
            head = head.next;
        }
        return result;
    }

    // Test cases and main function
    public static void main(String[] args) {
        int[][] testCases = {
                {1, 2, 3, 4, 5},
                {1},
                {1, 2},
                {1, 2},
                {1, 2, 3},
        };
        int[] ns = {2, 1, 1, 2, 3};
        int[][] expectedResults = {
                {1, 2, 3, 5},
                {},
                {1},
                {2},
                {1, 2},
        };

        java.lang.reflect.Method[] methods = RemoveNthNodeFromEnd.class.getDeclaredMethods();
        List<java.lang.reflect.Method> testMethods = new ArrayList<>();

        for (java.lang.reflect.Method method : methods) {
            if (method.getName().startsWith("removeNthFromEnd") &&
                method.getReturnType() == ListNode.class) {
                testMethods.add(method);
            }
        }

        Collections.sort(testMethods, Comparator.comparing(java.lang.reflect.Method::getName));

        int questionNum = 1;
        for (java.lang.reflect.Method method : testMethods) {
            System.out.println("\nQ" + questionNum + ": " + method.getName());
            System.out.println("-".repeat(70));

            boolean allPassed = true;
            for (int i = 0; i < testCases.length; i++) {
                try {
                    ListNode head = arrayToLinkedList(testCases[i]);
                    ListNode result = (ListNode) method.invoke(null, head, ns[i]);
                    List<Integer> resultList = linkedListToArray(result);
                    List<Integer> expected = Arrays.asList(expectedResults[i]);

                    boolean passed = resultList.equals(expected);
                    allPassed = allPassed && passed;
                    String status = passed ? "✓" : "✗";
                    System.out.println("  " + status + " removeNthFromEnd(" +
                        Arrays.toString(testCases[i]) + ", " + ns[i] + ") = " +
                        resultList + " (expected: " + expected + ")");
                } catch (Exception e) {
                    System.out.println("  ✗ Error: " + e.getMessage());
                    allPassed = false;
                }
            }

            if (allPassed) {
                System.out.println("  All tests passed!");
            }

            questionNum++;
        }
    }
}
