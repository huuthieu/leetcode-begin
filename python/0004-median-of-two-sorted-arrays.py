"""
LeetCode 0004: Median of Two Sorted Arrays

Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

# Practice Questions and Answers

# Q1: What's the brute force approach and its time complexity?
# A1: Merge both arrays and find median. Time: O(m+n), Space: O(m+n)
def findMedianSortedArrays_brute_force(nums1, nums2):
    merged = []
    i, j = 0, 0

    # Merge two sorted arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    # Find median
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]

# Q2: Can we find median without fully merging arrays?
# A2: Yes! We only need to find middle elements. Time: O(m+n), Space: O(1)
def findMedianSortedArrays_optimized_merge(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2

    i, j = 0, 0
    prev, curr = 0, 0

    # Iterate until we reach the middle
    for _ in range(half + 1):
        prev = curr

        if i < m and (j >= n or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1

    # Return median based on odd/even total length
    if total % 2 == 0:
        return (prev + curr) / 2
    else:
        return curr

# Q3: How can we achieve O(log(m+n)) time complexity?
# A3: Use binary search on the smaller array. Find the correct partition.
def findMedianSortedArrays_binary_search(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        # Get max elements on left side
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]

        # Get min elements on right side
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        # Check if we found the correct partition
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # If total length is even
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    raise ValueError("Input arrays are not sorted")

# Q4: What if one array is empty?
# A4: Handle edge case where one array is empty
def findMedianSortedArrays_with_empty_check(nums1, nums2):
    if not nums1:
        n = len(nums2)
        if n % 2 == 0:
            return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
        return nums2[n // 2]

    if not nums2:
        m = len(nums1)
        if m % 2 == 0:
            return (nums1[m // 2 - 1] + nums1[m // 2]) / 2
        return nums1[m // 2]

    # Use binary search approach
    return findMedianSortedArrays_binary_search(nums1, nums2)

# Q5: How does the binary search partitioning work?
"""
A5: The key insight is to partition both arrays such that:
- All elements on the left are smaller than all elements on the right
- The left partition has the same number of elements as right (or one more)

For correct partition:
- maxLeft1 <= minRight2
- maxLeft2 <= minRight1

If these conditions are met, the median is:
- Odd total length: max(maxLeft1, maxLeft2)
- Even total length: (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
"""

# Q6: What's the step-by-step process for binary search approach?
def findMedianSortedArrays_detailed(nums1, nums2):
    """
    Step 1: Ensure nums1 is smaller (for efficiency)
    Step 2: Binary search on nums1 to find partition point
    Step 3: Calculate corresponding partition in nums2
    Step 4: Check if partition is valid
    Step 5: Return median based on partition
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    imin, imax = 0, m
    half_len = (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums2[j - 1] > nums1[i]:
            # i is too small, increase it
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            # i is too big, decrease it
            imax = i - 1
        else:
            # Found the correct partition
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0

    return 0.0

# Q7: How do we handle arrays of very different sizes?
# A7: Always binary search on the smaller array (already handled in our solution)
def findMedianSortedArrays_size_optimized(nums1, nums2):
    # This automatically chooses the smaller array for binary search
    return findMedianSortedArrays_binary_search(nums1, nums2)

# Q8: What are common mistakes in this problem?
"""
A8: Common mistakes include:
1. Not handling empty arrays
2. Not ensuring binary search on smaller array
3. Off-by-one errors in partition calculation
4. Not handling edge cases (i=0, i=m, j=0, j=n)
5. Integer division issues with odd/even lengths
6. Incorrect median calculation for even total length
"""

# Q9: Can we use a different approach with heaps?
# A9: Yes, but it won't meet the O(log(m+n)) requirement
from heapq import heappush, heappop

def findMedianSortedArrays_heap(nums1, nums2):
    """
    Using two heaps approach (similar to Find Median from Data Stream)
    Time: O(m+n), Space: O(m+n)
    This doesn't meet the optimal time complexity requirement.
    """
    max_heap = []  # Left half (max heap)
    min_heap = []  # Right half (min heap)

    for num in nums1 + nums2:
        if not max_heap or num <= -max_heap[0]:
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)

        # Balance heaps
        if len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))

    if len(max_heap) > len(min_heap):
        return -max_heap[0]
    return (-max_heap[0] + min_heap[0]) / 2

# Q10: What are related problems and variations?
"""
A10: Related problems include:
- Find Kth Smallest Element in Two Sorted Arrays
- Find Median from Data Stream
- Merge K Sorted Arrays
- Kth Smallest Element in a Sorted Matrix
- Find Median in a Row-wise Sorted Matrix

Key concepts:
- Binary search on answer space
- Two pointers technique
- Heap-based approaches
- Partitioning strategies
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5.5),
        ([1, 2], [1, 2], 1.5),
        ([1], [2, 3, 4, 5], 3.0),
    ]

    print("Testing Binary Search Solution (Optimal):")
    for nums1, nums2, expected in test_cases:
        result = findMedianSortedArrays_binary_search(nums1, nums2)
        print(f"Input: nums1={nums1}, nums2={nums2}")
        print(f"Output: {result:.5f}, Expected: {expected:.5f}")
        print(f"Correct: {abs(result - expected) < 1e-5}")
        print()
