"""
LeetCode 155: Min Stack

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Time Complexity: O(1) for all operations
Space Complexity: O(n) where n is number of elements
"""


# Approach 1: Two Stacks - OPTIMAL and Most Intuitive
class MinStack:
    """
    Use two stacks:
    1. Main stack: stores all values
    2. Min stack: stores minimum values

    For each push:
    - Always push to main stack
    - Push to min stack if it's empty or value <= current min

    For each pop:
    - Always pop from main stack
    - Pop from min stack if popped value == current min

    Time: O(1) for all operations
    Space: O(n) in worst case (all elements in both stacks)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if it's empty or val is new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # Remove from min_stack if it was the minimum
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


# Approach 2: Single Stack with Tuples
class MinStack2:
    """
    Store tuples of (value, current_minimum) in a single stack
    Each element knows what the minimum was when it was pushed

    Time: O(1) for all operations
    Space: O(n) - each element stores a tuple
    """

    def __init__(self):
        self.stack = []  # Each element is (val, min_at_this_point)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Approach 3: Single Stack with Difference Tracking
class MinStack3:
    """
    Store differences from minimum instead of actual values
    This is a space-optimized approach but more complex

    - When pushing, store difference from current min
    - Update min if new value is smaller
    - Reconstruct actual values when needed

    Time: O(1) for all operations
    Space: O(n) but potentially saves space for large numbers

    Note: This approach is tricky and not recommended for interviews
    unless specifically asked for space optimization
    """

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            diff = val - self.min_val
            self.stack.append(diff)
            if val < self.min_val:
                self.min_val = val

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:  # The popped element was the minimum
                self.min_val = self.min_val - diff

    def top(self) -> int:
        if self.stack:
            diff = self.stack[-1]
            if diff < 0:
                return self.min_val
            else:
                return self.min_val + diff
        return None

    def getMin(self) -> int:
        return self.min_val


# Approach 4: Linked List Based (for comparison)
class Node:
    def __init__(self, val, min_val, next_node=None):
        self.val = val
        self.min = min_val
        self.next = next_node


class MinStack4:
    """
    Use a linked list where each node stores its value and the minimum up to that point

    Time: O(1) for all operations
    Space: O(n)
    """

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, val)
        else:
            min_val = min(val, self.head.min)
            new_node = Node(val, min_val, self.head)
            self.head = new_node

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next

    def top(self) -> int:
        return self.head.val if self.head else None

    def getMin(self) -> int:
        return self.head.min if self.head else None


# Test Cases
def test_min_stack():
    print("Testing MinStack Implementations:\n")

    # Test all implementations
    implementations = [
        (MinStack, "Two Stacks Approach"),
        (MinStack2, "Single Stack with Tuples"),
        (MinStack3, "Difference Tracking"),
        (MinStack4, "Linked List Based"),
    ]

    for StackClass, name in implementations:
        print(f"Testing {name}:")

        # Test Case 1: Basic operations
        minStack = StackClass()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)

        assert minStack.getMin() == -3, f"{name}: getMin failed"
        assert minStack.top() == -3, f"{name}: top failed"

        minStack.pop()
        assert minStack.top() == 0, f"{name}: top after pop failed"
        assert minStack.getMin() == -2, f"{name}: getMin after pop failed"

        print(f"  [PASS] Basic operations")

        # Test Case 2: All same values
        minStack2 = StackClass()
        minStack2.push(5)
        minStack2.push(5)
        minStack2.push(5)

        assert minStack2.getMin() == 5, f"{name}: same values getMin failed"
        minStack2.pop()
        assert minStack2.getMin() == 5, f"{name}: same values after pop failed"

        print(f"  [PASS] All same values")

        # Test Case 3: Ascending order
        minStack3 = StackClass()
        minStack3.push(1)
        minStack3.push(2)
        minStack3.push(3)
        minStack3.push(4)

        assert minStack3.getMin() == 1, f"{name}: ascending getMin failed"
        minStack3.pop()
        minStack3.pop()
        assert minStack3.getMin() == 1, f"{name}: ascending after pops failed"

        print(f"  [PASS] Ascending order")

        # Test Case 4: Descending order
        minStack4 = StackClass()
        minStack4.push(4)
        minStack4.push(3)
        minStack4.push(2)
        minStack4.push(1)

        assert minStack4.getMin() == 1, f"{name}: descending getMin failed"
        minStack4.pop()
        assert minStack4.getMin() == 2, f"{name}: descending after pop failed"
        minStack4.pop()
        assert minStack4.getMin() == 3, f"{name}: descending after 2 pops failed"

        print(f"  [PASS] Descending order")

        # Test Case 5: Negative numbers
        minStack5 = StackClass()
        minStack5.push(-5)
        minStack5.push(-2)
        minStack5.push(-8)
        minStack5.push(-1)

        assert minStack5.getMin() == -8, f"{name}: negative numbers getMin failed"
        minStack5.pop()
        assert minStack5.getMin() == -8, f"{name}: negative after pop failed"
        minStack5.pop()
        assert minStack5.getMin() == -5, f"{name}: negative after 2 pops failed"

        print(f"  [PASS] Negative numbers")

        # Test Case 6: Large numbers
        minStack6 = StackClass()
        minStack6.push(2147483647)
        minStack6.push(-2147483648)
        minStack6.push(0)

        assert minStack6.getMin() == -2147483648, f"{name}: large numbers getMin failed"

        print(f"  [PASS] Large numbers")

        print(f"  All tests passed for {name}!\n")


# Practice Questions
def practice_questions():
    """
    Q1: Why do we need <= instead of < when pushing to min_stack?
    A1: Because we need to handle duplicate minimums. If we only use <,
        when we pop a minimum that appears twice, we'd lose track of it.
        Example: push(1), push(1), pop() should still have min=1.

    Q2: What's the worst-case space complexity?
    A2: O(n) for the two-stack approach. In the worst case (descending order),
        every element is a new minimum, so both stacks have n elements.

    Q3: Can we optimize space further?
    A3: Yes, using the difference tracking approach (MinStack3), but it's
        more complex and error-prone. For interviews, the two-stack approach
        is preferred for its simplicity and clarity.

    Q4: What if we need to support getMax() as well?
    A4: Add another stack (max_stack) that works the same way as min_stack.
        Or use the tuple approach and store (val, min, max).

    Q5: Why is the tuple approach using O(n) space if each element stores a tuple?
    A5: Each element stores exactly one integer worth of extra information
        (the minimum at that point), so it's still O(n) overall, just with
        a constant factor of 2.

    Q6: How would you implement this in a thread-safe manner?
    A6: Add locks/semaphores to each method to ensure mutual exclusion.
        In Python, use threading.Lock() and with self.lock: for each method.

    Q7: What are real-world applications?
    A7: - Browser history with quick access to most visited page
        - Stock price tracking with running minimum
        - Undo/redo functionality with metadata tracking
        - Expression evaluation with min/max tracking

    Q8: Can we use a single variable to track the minimum?
    A8: No, because when we pop the minimum, we need to know what the
        previous minimum was. We need to store historical minimum values.

    Q9: What if we need to support getMin() for any arbitrary position in the stack?
    A9: Use a segment tree or a balanced BST to support range minimum queries.
        This would increase time complexity to O(log n) but allow more flexibility.

    Q10: How does this relate to the monotonic stack pattern?
    A10: Min stack maintains a monotonic non-increasing stack in min_stack.
         This is similar to problems like "next greater element" or
         "largest rectangle in histogram" which use monotonic stacks.
    """
    pass


# Follow-up Problems
def follow_up_problems():
    """
    1. Max Stack: Implement a stack with getMax() operation
       Solution: Same approach, use max_stack instead of min_stack

    2. Min Queue: Implement a queue with getMin() operation
       Solution: Use two stacks, implement queue using stacks + min tracking

    3. Median Stack: Implement a stack with getMedian() operation
       Solution: Use two heaps (max heap for lower half, min heap for upper half)

    4. kth Smallest in Stack: Find kth smallest element
       Solution: Additional data structure like BST or sorted list

    5. Min Stack with Frequency: Track minimum and its frequency
       Solution: Store (value, count) in min_stack
    """
    pass


if __name__ == "__main__":
    test_min_stack()
    print("="*50)
    print("All implementations passed all tests!")
    print("="*50)

    # Uncomment to see practice questions
    # help(practice_questions)
    # help(follow_up_problems)
