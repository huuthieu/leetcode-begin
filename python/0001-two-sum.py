"""
LeetCode 0001: Two Sum

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

# Practice Questions and Answers

# Q1: What's the brute force approach and its time complexity?
# A1: Check every pair of numbers. Time: O(n^2), Space: O(1)
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Q2: How can we optimize using a hash map?
# A2: Store complement values with indices. Time: O(n), Space: O(n)
def two_sum_hash_map(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Q3: What if we need to return the actual values instead of indices?
# A3: Same logic, but return the values
def two_sum_values(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen[num] = True
    return []

# Q4: What if the array is sorted? Can we do better than O(n) space?
# A4: Use two pointers approach. Time: O(n), Space: O(1)
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Q5: What if there are multiple valid pairs? Return all of them.
# A5: Continue searching instead of returning immediately
def two_sum_all_pairs(nums, target):
    seen = {}
    result = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            for j in seen[complement]:
                result.append([j, i])
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    return result

# Q6: What about edge cases we should consider?
# A6: Empty array, single element, no solution, duplicate numbers
def two_sum_with_validation(nums, target):
    if not nums or len(nums) < 2:
        return []
    
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Q7: How would you handle very large numbers or potential overflow?
# A7: Python handles big integers automatically, but in other languages:
def two_sum_safe(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        try:
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        except OverflowError:
            continue
    return []

# Q8: What's the space-time tradeoff analysis?
"""
A8: 
Brute Force: O(n^2) time, O(1) space
Hash Map: O(n) time, O(n) space
Two Pointers (sorted): O(n) time, O(1) space (but requires sorted array)

The hash map approach is generally preferred for unsorted arrays.
"""

# Q9: How would you implement this without using built-in hash maps?
# A9: Use a simple list-based approach (less efficient)
def two_sum_no_hashmap(nums, target):
    seen = []
    indices = []
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            complement_index = seen.index(complement)
            return [indices[complement_index], i]
        seen.append(num)
        indices.append(i)
    return []

# Q10: What variations of this problem exist?
"""
A10: Common variations include:
- Two Sum II (sorted array)
- Three Sum
- Four Sum
- Two Sum with BST
- Two Sum with duplicates allowed
- Two Sum closest to target
- Two Sum in a stream of data
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([-1, -2, -3, -4, -5], -8, [2, 4])
    ]
    
    for nums, target, expected in test_cases:
        result = two_sum_hash_map(nums, target)
        print(f"Input: nums={nums}, target={target}")
        print(f"Output: {result}, Expected: {expected}")
        print(f"Correct: {sorted(result) == sorted(expected)}")
        print()
