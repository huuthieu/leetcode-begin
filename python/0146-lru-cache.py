"""
LeetCode 146: LRU Cache

Problem:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists.
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
"""

# Approach 1: HashMap + Doubly Linked List - OPTIMAL
class DLLNode:
    """Node for doubly linked list"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    Use HashMap for O(1) lookup and Doubly Linked List for O(1) insertion/deletion

    Key insights:
    - HashMap: key -> node (for O(1) access)
    - Doubly Linked List: maintains order of usage
      * Head: most recently used
      * Tail: least recently used
    - Dummy head and tail nodes simplify edge case handling

    Operations:
    - get(key): Move accessed node to head (most recent)
    - put(key, value): Add/update node at head, evict from tail if over capacity

    Time: O(1) for get and put
    Space: O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DLLNode

        # Dummy head and tail to simplify edge cases
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLLNode) -> None:
        """Remove a node from the doubly linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: DLLNode) -> None:
        """Add a node right after the head (most recently used position)"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: DLLNode) -> None:
        """Move an existing node to the head (mark as recently used)"""
        self._remove(node)
        self._add_to_head(node)

    def _pop_tail(self) -> DLLNode:
        """Remove and return the least recently used node (before tail)"""
        lru = self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key: int) -> int:
        """Get value for key, return -1 if not found. Mark key as recently used."""
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)  # Mark as recently used
        return node.value

    def put(self, key: int, value: int) -> None:
        """Put key-value pair. If key exists, update value. If over capacity, evict LRU."""
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)  # Mark as recently used
        else:
            # Add new key
            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            if len(self.cache) > self.capacity:
                # Evict least recently used
                lru = self._pop_tail()
                del self.cache[lru.key]


# Approach 2: Using OrderedDict (Python-specific, but good to know)
from collections import OrderedDict


class LRUCache2:
    """
    Python's OrderedDict maintains insertion order and allows moving items to end

    - get: Move accessed item to end (most recent)
    - put: Add/update item at end, remove first item if over capacity

    Time: O(1) for get and put
    Space: O(capacity)

    Note: This is a cleaner implementation but uses Python's built-in data structure.
    In interviews, implement Approach 1 to show understanding of underlying concepts.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used (first item)


# Approach 3: Manual OrderedDict Implementation
class Node3:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache3:
    """
    Another implementation of doubly linked list + hashmap
    with slightly different structure for educational comparison

    Time: O(1) for get and put
    Space: O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def _remove_node(self, node: Node3) -> None:
        """Remove a node from the list"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def _add_to_front(self, node: Node3) -> None:
        """Add node to front of list"""
        node.next = self.head
        node.prev = None

        if self.head:
            self.head.prev = node

        self.head = node

        if not self.tail:
            self.tail = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove_node(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_front(node)
        else:
            new_node = Node3(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

            if len(self.cache) > self.capacity:
                del self.cache[self.tail.key]
                self._remove_node(self.tail)


# Test Cases
def test_lru_cache():
    print("Testing LRU Cache Implementations:\n")

    implementations = [
        (LRUCache, "HashMap + Doubly Linked List"),
        (LRUCache2, "OrderedDict"),
        (LRUCache3, "Manual Implementation"),
    ]

    for CacheClass, name in implementations:
        print(f"Testing {name}:")

        # Test Case 1: Basic operations from problem example
        cache = CacheClass(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1, f"{name}: get(1) failed"

        cache.put(3, 3)  # Evicts key 2
        assert cache.get(2) == -1, f"{name}: get(2) should return -1"

        cache.put(4, 4)  # Evicts key 1
        assert cache.get(1) == -1, f"{name}: get(1) should return -1"
        assert cache.get(3) == 3, f"{name}: get(3) failed"
        assert cache.get(4) == 4, f"{name}: get(4) failed"

        print(f"  [PASS] Basic operations")

        # Test Case 2: Update existing key
        cache2 = CacheClass(2)
        cache2.put(1, 1)
        cache2.put(2, 2)
        cache2.put(1, 10)  # Update key 1
        assert cache2.get(1) == 10, f"{name}: update failed"

        cache2.put(3, 3)  # Should evict key 2 (not key 1 since it was just updated)
        assert cache2.get(2) == -1, f"{name}: should evict key 2"
        assert cache2.get(1) == 10, f"{name}: key 1 should still exist"

        print(f"  [PASS] Update existing key")

        # Test Case 3: Single capacity
        cache3 = CacheClass(1)
        cache3.put(1, 1)
        assert cache3.get(1) == 1, f"{name}: single capacity get failed"

        cache3.put(2, 2)  # Evicts key 1
        assert cache3.get(1) == -1, f"{name}: key 1 should be evicted"
        assert cache3.get(2) == 2, f"{name}: key 2 should exist"

        print(f"  [PASS] Single capacity")

        # Test Case 4: Access pattern affects eviction
        cache4 = CacheClass(2)
        cache4.put(1, 1)
        cache4.put(2, 2)
        cache4.get(1)  # Access key 1, making key 2 the LRU
        cache4.put(3, 3)  # Should evict key 2
        assert cache4.get(2) == -1, f"{name}: key 2 should be evicted"
        assert cache4.get(1) == 1, f"{name}: key 1 should exist"
        assert cache4.get(3) == 3, f"{name}: key 3 should exist"

        print(f"  [PASS] Access pattern affects eviction")

        # Test Case 5: Multiple updates
        cache5 = CacheClass(2)
        cache5.put(1, 1)
        cache5.put(1, 2)
        cache5.put(1, 3)
        cache5.put(2, 2)
        cache5.put(2, 4)
        assert cache5.get(1) == 3, f"{name}: multiple updates for key 1 failed"
        assert cache5.get(2) == 4, f"{name}: multiple updates for key 2 failed"

        print(f"  [PASS] Multiple updates")

        # Test Case 6: Large capacity
        cache6 = CacheClass(3)
        cache6.put(1, 1)
        cache6.put(2, 2)
        cache6.put(3, 3)
        assert cache6.get(1) == 1, f"{name}: large capacity failed"
        assert cache6.get(2) == 2, f"{name}: large capacity failed"
        assert cache6.get(3) == 3, f"{name}: large capacity failed"

        cache6.put(4, 4)  # Should evict key 1 (LRU after gets in order)
        # Actually, after the gets above, order is 3 (MRU) -> 2 -> 1 (LRU)
        # Wait, after get(1), get(2), get(3), order should be 3 -> 2 -> 1
        # So putting 4 should evict... let me reconsider
        # Initially: 1, 2, 3 (in insertion order)
        # get(1): 1 moves to MRU: 1, 2, 3 (1 is MRU)
        # get(2): 2 moves to MRU: 2, 1, 3 (2 is MRU)
        # get(3): 3 moves to MRU: 3, 2, 1 (3 is MRU, 1 is LRU)
        # put(4): evicts 1
        assert cache6.get(1) == -1, f"{name}: key 1 should be evicted"
        assert cache6.get(4) == 4, f"{name}: key 4 should exist"

        print(f"  [PASS] Large capacity")

        print(f"  All tests passed for {name}!\n")


# Practice Questions
def practice_questions():
    """
    Q1: Why do we need both a HashMap and a Doubly Linked List?
    A1: HashMap gives O(1) lookup by key. Doubly Linked List gives O(1)
        insertion/deletion and maintains the order of usage. We need both
        to achieve O(1) for all operations.

    Q2: Why doubly linked list instead of singly linked list?
    A2: We need to remove nodes from the middle when they're accessed.
        With singly linked list, finding the previous node takes O(n).
        Doubly linked list gives O(1) removal.

    Q3: Why use dummy head and tail nodes?
    A3: They eliminate special cases for empty list and single-node list.
        Without them, we'd need to check if head/tail is None and handle
        separately, making code more error-prone.

    Q4: What's the space complexity?
    A4: O(capacity). We store at most 'capacity' nodes in both the HashMap
        and the Doubly Linked List.

    Q5: How would you implement LRU cache with TTL (time-to-live)?
    A5: Add a timestamp field to each node. In get/put, check if current
        time - timestamp > TTL. If so, treat as cache miss and remove.
        Could also use a min-heap to track expiration times.

    Q6: How to make this thread-safe?
    A6: Add a lock (threading.Lock()) and wrap all public methods with it.
        For better performance, use a ReadWriteLock to allow concurrent reads.

    Q7: What are real-world applications?
    A7: - Browser cache (recently visited pages)
        - Database query result cache
        - CDN caching
        - CPU cache management
        - DNS cache
        - Application-level caching (Redis, Memcached)

    Q8: How to implement LFU (Least Frequently Used) cache?
    A8: Track access frequency for each key. Use a HashMap + min-heap,
        or HashMap + doubly linked list with frequency buckets.

    Q9: What if we need to support a "peek" operation that doesn't update recency?
    A9: Add a peek method that returns the value without calling _move_to_head.

    Q10: How would you handle cache invalidation?
    A10: Add a delete(key) method that removes the key from both the HashMap
         and the Doubly Linked List. Could also add invalidate_all() to clear cache.
    """
    pass


# Follow-up Problems
def follow_up_problems():
    """
    1. LFU Cache (LeetCode 460): Track access frequency instead of recency
       Solution: Use HashMap + frequency buckets with doubly linked lists

    2. LRU Cache with TTL: Items expire after a time period
       Solution: Add timestamp to nodes, clean up on access

    3. Time-Based Key-Value Store (LeetCode 981): Get value at specific timestamp
       Solution: HashMap of key -> [(timestamp, value)] with binary search

    4. LRU Cache with Priority: Some items have higher priority and shouldn't be evicted
       Solution: Separate lists for different priorities

    5. Distributed LRU Cache: LRU cache across multiple servers
       Solution: Consistent hashing + local LRU on each node

    6. 2Q Cache: Improvement over LRU with two queues
       Solution: One queue for first access, another for repeated accesses
    """
    pass


if __name__ == "__main__":
    test_lru_cache()
    print("="*50)
    print("All implementations passed all tests!")
    print("="*50)

    # Uncomment to see practice questions
    # help(practice_questions)
    # help(follow_up_problems)
