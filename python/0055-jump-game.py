"""
LeetCode 55: Jump Game

Problem:
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length
is 0, which makes it impossible to reach the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

Time Complexity: O(n) for greedy approach
Space Complexity: O(1) for greedy approach
"""


# Approach 1: Greedy (Optimal) - Track Max Reachable Position
def canJump_greedy(nums):
    """
    Track the maximum position we can reach

    Key insight: We don't need to track all possible paths.
    We only need to know if we can reach the end.

    Algorithm:
    - Keep track of the furthest position we can reach
    - For each position, if we can reach it, update max reachable
    - If we can reach or pass the last index, return True

    Time: O(n) - single pass
    Space: O(1) - only storing max_reach
    """
    max_reach = 0

    for i in range(len(nums)):
        # If current position is beyond max reachable, we're stuck
        if i > max_reach:
            return False

        # Update max reachable position
        max_reach = max(max_reach, i + nums[i])

        # Early termination: if we can reach the end
        if max_reach >= len(nums) - 1:
            return True

    return True


# Approach 2: Greedy (Backward) - Work from End
def canJump_backward(nums):
    """
    Start from the end and work backward

    Key insight: If we can reach position i from some earlier position,
    then we only need to check if we can reach that earlier position.

    Algorithm:
    - Start with goal = last index
    - Move backward: if we can reach goal from current position,
      update goal to current position
    - Return True if goal reaches index 0

    Time: O(n)
    Space: O(1)
    """
    goal = len(nums) - 1

    # Work backward from second-to-last element
    for i in range(len(nums) - 2, -1, -1):
        # Can we reach the goal from position i?
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


# Approach 3: Dynamic Programming (Bottom-Up)
def canJump_dp(nums):
    """
    Use DP array where dp[i] = True if we can reach index i

    Time: O(n^2) in worst case
    Space: O(n)

    Note: This is less efficient than greedy but shows DP thinking
    """
    n = len(nums)
    dp = [False] * n
    dp[0] = True  # We start at index 0

    for i in range(n):
        if not dp[i]:
            continue  # Can't reach this position

        # From position i, we can jump to any position within nums[i] steps
        for j in range(i + 1, min(i + nums[i] + 1, n)):
            dp[j] = True

        # Early termination
        if dp[n - 1]:
            return True

    return dp[n - 1]


# Approach 4: BFS (Less efficient but shows different thinking)
def canJump_bfs(nums):
    """
    Treat as graph problem: each index is a node,
    edges connect to reachable positions

    Time: O(n) in best case, O(n^2) in worst case
    Space: O(n) for queue
    """
    from collections import deque

    if len(nums) == 1:
        return True

    queue = deque([0])
    visited = {0}

    while queue:
        pos = queue.popleft()

        # Try all possible jumps from current position
        for next_pos in range(pos + 1, min(pos + nums[pos] + 1, len(nums))):
            if next_pos == len(nums) - 1:
                return True

            if next_pos not in visited:
                visited.add(next_pos)
                queue.append(next_pos)

    return False


# Follow-up 1: Jump Game II - Find minimum number of jumps to reach end
def jump_min_jumps(nums):
    """
    Find minimum number of jumps to reach the last index

    Greedy approach: Always jump to the position that lets us reach furthest

    Time: O(n)
    Space: O(1)
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0  # End of range for current jump
    farthest = 0  # Farthest position reachable

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        # If we've reached the end of current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest

            # Early termination
            if current_end >= len(nums) - 1:
                break

    return jumps


# Follow-up 2: Check if we can reach specific index
def canReachIndex(nums, target):
    """
    Check if we can reach a specific target index

    Time: O(n)
    Space: O(1)
    """
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])

        if max_reach >= target:
            return True

    return False


# Follow-up 3: Find all positions we can reach
def findReachablePositions(nums):
    """
    Return list of all indices we can reach

    Time: O(n)
    Space: O(n) for result
    """
    reachable = [False] * len(nums)
    reachable[0] = True
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            break

        max_reach = max(max_reach, i + nums[i])

        for j in range(i + 1, min(max_reach + 1, len(nums))):
            reachable[j] = True

    return [i for i in range(len(nums)) if reachable[i]]


# Test Cases
def test_jump_game():
    print("Testing Jump Game:\n")

    test_cases = [
        ([2, 3, 1, 1, 4], True, "Can reach end with multiple paths"),
        ([3, 2, 1, 0, 4], False, "Stuck at index 3 with 0"),
        ([0], True, "Single element, already at end"),
        ([1, 0, 1, 0], False, "Can't pass first 0"),
        ([1, 1, 1, 1], True, "All 1s, step by step"),
        ([2, 0, 0], True, "Jump over zeros"),
        ([1, 2, 3], True, "Increasing jumps"),
        ([5, 4, 3, 2, 1, 0], True, "First jump reaches end"),
        ([1, 0, 2], False, "Stuck at 0"),
        ([2, 5, 0, 0], True, "Long jump"),
    ]

    for nums, expected, description in test_cases:
        result1 = canJump_greedy(nums)
        result2 = canJump_backward(nums)
        result3 = canJump_dp(nums)
        result4 = canJump_bfs(nums)

        assert result1 == expected, f"Greedy forward failed for {description}"
        assert result2 == expected, f"Greedy backward failed for {description}"
        assert result3 == expected, f"DP failed for {description}"
        assert result4 == expected, f"BFS failed for {description}"

        print(f"[PASS] {description}")
        print(f"       nums = {nums}, can reach end = {expected}\n")

    print("\nTesting Jump Game II (Minimum Jumps):\n")

    min_jump_cases = [
        ([2, 3, 1, 1, 4], 2),  # 0 -> 1 -> 4
        ([2, 3, 0, 1, 4], 2),  # 0 -> 1 -> 4
        ([1, 1, 1, 1], 3),  # 0 -> 1 -> 2 -> 3
        ([1, 2, 3], 2),  # 0 -> 1 -> 3 or 0 -> 2 -> 3
        ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], 3),  # 0 -> 1 -> 5 -> 11
    ]

    for nums, expected in min_jump_cases:
        result = jump_min_jumps(nums)
        assert result == expected, f"Min jumps failed: got {result}, expected {expected}"
        print(f"[PASS] nums = {nums}")
        print(f"       min jumps = {expected}\n")


# Practice Questions
def practice_questions():
    """
    Q1: Why is the greedy approach optimal?
    A1: At each position, we only care about the furthest position we can reach.
        We don't need to track all possible paths because if we can reach position X,
        it doesn't matter how we got there - we have the same options going forward.

    Q2: What's the difference between forward and backward greedy?
    A2: Forward: Track max reachable position moving forward.
        Backward: Start from end, move backward updating the closest position
        that can reach the goal. Both are O(n) and O(1) space.

    Q3: Why is DP less efficient here?
    A3: DP is O(n^2) because for each position, we might need to check all
        positions we can jump to. Greedy is O(n) because we only track the
        maximum reachable position.

    Q4: When would we use BFS instead of greedy?
    A4: BFS is useful when we need the actual path or when jump rules are more
        complex (e.g., we can only jump to positions with certain values).
        For this problem, greedy is better.

    Q5: How to reconstruct the actual jump sequence?
    A5: Modify the greedy approach to store the parent of each reachable position.
        Then backtrack from the end to construct the path.

    Q6: What if we can jump backward as well?
    A6: Greedy won't work. Use BFS/DFS to explore all directions, or DP where
        dp[i] considers jumps from both left and right.

    Q7: What if each position has both min and max jump lengths?
    A7: Use BFS/DFS to explore valid jumps. Greedy might not work because
        we might need to take shorter jumps to reach certain positions.

    Q8: Real-world applications?
    A8: - Video game level design (can player reach the end?)
        - Network routing (can packets reach destination?)
        - Resource allocation (can we complete all tasks with given resources?)
        - Chess piece movement (can piece reach square?)

    Q9: How to handle negative numbers in array?
    A9: Negative numbers would mean "jump backward". This changes the problem
        significantly - would need BFS/DFS to handle cycles and track visited nodes.

    Q10: What's the maximum number of jumps needed in worst case?
    A10: O(n) jumps if the array is all 1s. Best case is 1 jump if nums[0] >= n-1.
    """
    pass


# Follow-up Problems
def follow_up_problems():
    """
    1. LeetCode 45: Jump Game II - Find minimum number of jumps
       Solution: Greedy with BFS-like levels, O(n) time

    2. LeetCode 1306: Jump Game III - Can reach value 0? (can jump forward or backward)
       Solution: BFS/DFS with visited set

    3. LeetCode 1871: Jump Game VII - Can reach end with constraints on where to land
       Solution: Sliding window + DP

    4. LeetCode 1345: Jump Game IV - Jump to indices with same value
       Solution: BFS with HashMap

    5. LeetCode 1340: Jump Game V - Max visits with constraint (can jump to smaller values)
       Solution: DFS with memoization

    6. Minimum jumps to reach end with jump cost
       Solution: DP with cost tracking

    7. Maximum coins collected while jumping
       Solution: DP, dp[i] = max coins reaching position i
    """
    pass


if __name__ == "__main__":
    test_jump_game()
    print("="*50)
    print("All tests passed!")
    print("="*50)

    # Uncomment to see practice questions
    # help(practice_questions)
    # help(follow_up_problems)
