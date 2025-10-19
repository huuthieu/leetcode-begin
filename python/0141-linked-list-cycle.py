"""
LeetCode 141: Linked List Cycle

Problem:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

Time Complexity: O(n)
Space Complexity: O(1) for Floyd's, O(n) for hash set
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach 1: Floyd's Cycle Detection (Tortoise and Hare) - OPTIMAL
def hasCycle_Floyd(head):
    """
    Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
    If there's a cycle, fast will eventually meet slow
    If there's no cycle, fast will reach the end

    Time: O(n) - In worst case, slow pointer traverses all nodes once
    Space: O(1) - Only two pointers used

    Why this works:
    - If there's a cycle, both pointers will be inside the cycle eventually
    - Fast pointer moves 1 node closer to slow pointer each iteration
    - They will eventually meet
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next           # Move 1 step
        fast = fast.next.next      # Move 2 steps

        if slow == fast:           # Cycle detected
            return True

    return False                   # Reached end, no cycle


# Approach 2: Hash Set
def hasCycle_HashSet(head):
    """
    Keep track of visited nodes in a set
    If we see a node again, there's a cycle

    Time: O(n) - Visit each node once
    Space: O(n) - Store all nodes in set
    """
    if not head:
        return False

    visited = set()
    current = head

    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next

    return False


# Approach 3: Marking Nodes (Destructive - modifies the list)
def hasCycle_Marking(head):
    """
    Mark visited nodes by changing their value to a sentinel
    Not recommended as it modifies the original list

    Time: O(n)
    Space: O(1)

    Note: This approach is shown for educational purposes but should
    NOT be used in practice as it destroys the original data
    """
    if not head:
        return False

    sentinel = float('inf')
    current = head

    while current:
        if current.val == sentinel:
            return True
        current.val = sentinel
        current = current.next

    return False


# Follow-up Question 1: Find the start of the cycle
def detectCycle(head):
    """
    Return the node where the cycle begins. If no cycle, return None.

    Algorithm:
    1. Use Floyd's algorithm to detect cycle
    2. If cycle exists, reset one pointer to head
    3. Move both pointers one step at a time
    4. They will meet at the cycle start

    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return None

    # Phase 1: Detect cycle
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Follow-up Question 2: Find the length of the cycle
def cycleLength(head):
    """
    Return the length of the cycle. If no cycle, return 0.

    Algorithm:
    1. Use Floyd's algorithm to detect cycle
    2. Once detected, keep one pointer fixed and move the other
    3. Count steps until they meet again

    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return 0

    # Phase 1: Detect cycle
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return 0

    # Phase 2: Count cycle length
    length = 1
    current = slow.next

    while current != slow:
        length += 1
        current = current.next

    return length


# Helper function to create linked list with cycle
def create_linked_list_with_cycle(values, pos):
    """
    Create a linked list with a cycle
    pos: index where tail connects (-1 for no cycle)
    """
    if not values:
        return None

    nodes = [ListNode(val) for val in values]

    # Connect nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle if pos >= 0
    if pos >= 0:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# Test Cases
def test_hasCycle():
    print("Testing Linked List Cycle Detection:\n")

    test_cases = [
        ([3, 2, 0, -4], 1, True, "Cycle at index 1"),
        ([1, 2], 0, True, "Cycle at index 0"),
        ([1], -1, False, "Single node, no cycle"),
        ([], -1, False, "Empty list"),
        ([1, 2, 3, 4, 5], 2, True, "Cycle at index 2"),
        ([1, 2, 3, 4, 5], -1, False, "No cycle"),
    ]

    for values, pos, expected, description in test_cases:
        # Test Floyd's algorithm
        head1 = create_linked_list_with_cycle(values, pos)
        result1 = hasCycle_Floyd(head1)

        # Test Hash Set
        head2 = create_linked_list_with_cycle(values, pos)
        result2 = hasCycle_HashSet(head2)

        assert result1 == expected, f"Floyd's failed for {description}"
        assert result2 == expected, f"HashSet failed for {description}"

        print(f"[PASS] {description}")
        print(f"  Input: {values}, pos = {pos}")
        print(f"  Expected: {expected}, Got: {result1}\n")

    print("\nTesting Cycle Start Detection:\n")

    # Test finding cycle start
    test_cases_start = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1, 2, 3, 4, 5], 2),
    ]

    for values, pos in test_cases_start:
        head = create_linked_list_with_cycle(values, pos)
        cycle_start = detectCycle(head)

        # Verify by checking the value
        expected_val = values[pos]
        actual_val = cycle_start.val if cycle_start else None

        assert actual_val == expected_val, f"Cycle start detection failed"
        print(f"[PASS] List {values}, cycle at index {pos}")
        print(f"  Cycle starts at node with value: {actual_val}\n")

    print("\nTesting Cycle Length:\n")

    # Test cycle length
    for values, pos in test_cases_start:
        head = create_linked_list_with_cycle(values, pos)
        length = cycleLength(head)
        expected_length = len(values) - pos

        assert length == expected_length, f"Cycle length detection failed"
        print(f"[PASS] List {values}, cycle at index {pos}")
        print(f"  Cycle length: {length}\n")


# Practice Questions
def practice_questions():
    """
    Q1: Why does Floyd's Cycle Detection algorithm work?
    A1: If there's a cycle, both pointers eventually enter it. The fast pointer
        moves 1 node closer to slow each iteration, so they must eventually meet.
        It's like two runners on a circular track where one runs twice as fast.

    Q2: What's the time complexity if there's a very long tail before the cycle?
    A2: Still O(n). Slow pointer needs to traverse the tail (let's say length L)
        and then at most the cycle length (C). Total: O(L + C) = O(n).

    Q3: Can we use fast pointer moving 3 steps instead of 2?
    A3: No, they might miss each other. With speed difference of 1, they're
        guaranteed to meet. With higher speed difference, fast might "jump over"
        slow in the cycle.

    Q4: What if the cycle starts at the head?
    A4: The algorithm still works. Both pointers enter the cycle immediately
        and will meet within the cycle.

    Q5: Why not just use a hash set?
    A5: Hash set uses O(n) space. Floyd's algorithm achieves O(1) space,
        which is better for memory-constrained environments.

    Q6: How to find the node where the cycle begins?
    A6: After detecting the cycle, reset one pointer to head. Move both one
        step at a time. They'll meet at the cycle start. This is because
        the distance from head to cycle start equals the distance from
        meeting point to cycle start (going around the cycle).

    Q7: What are real-world applications?
    A7: - Detecting infinite loops in program execution
        - Finding duplicate processes in OS scheduling
        - Detecting cycles in dependency graphs
        - Memory leak detection in garbage collection

    Q8: Can this algorithm be adapted for other data structures?
    A8: Yes! It can detect cycles in:
        - Arrays (where arr[i] points to arr[arr[i]])
        - Function iteration (f(f(f(...x))) finding a loop)
        - State machines (detecting infinite state loops)
    """
    pass


if __name__ == "__main__":
    test_hasCycle()
    print("\n" + "="*50)
    print("All tests passed!")
    print("="*50)

    # Uncomment to see practice questions
    # help(practice_questions)
