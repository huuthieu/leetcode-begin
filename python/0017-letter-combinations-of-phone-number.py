"""
LeetCode Problem 0017: Letter Combinations of a Phone Number

Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons):
- 2 -> "abc"
- 3 -> "def"
- 4 -> "ghi"
- 5 -> "jkl"
- 6 -> "mno"
- 7 -> "pqrs"
- 8 -> "tuv"
- 9 -> "wxyz"

Examples:
1. Input: digits = "23", Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "", Output: []
3. Input: digits = "2", Output: ["a","b","c"]
4. Input: digits = "234", Output: ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]

Constraints:
- 0 <= digits.length <= 4
- digits[i].isdigit() and digits[i] != '0' and digits[i] != '1'
"""

# Q1: Recursive backtracking
def letterCombinations_backtrack(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n) where n is length of digits
    Space Complexity: O(4^n) for result storage

    Approach: Use recursion to generate all combinations.
    """
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index, current):
        if index == len(digits):
            result.append(current)
            return

        letters = mapping[digits[index]]
        for letter in letters:
            backtrack(index + 1, current + letter)

    backtrack(0, "")
    return result


# Q2: Iterative approach
def letterCombinations_iterative(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: Build combinations iteratively.
    """
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = ['']

    for digit in digits:
        temp = []
        for combo in result:
            for letter in mapping[digit]:
                temp.append(combo + letter)
        result = temp

    return result


# Q3: BFS with queue
def letterCombinations_bfs(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: Use BFS with a queue.
    """
    if not digits:
        return []

    from collections import deque

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    queue = deque([''])

    for digit in digits:
        size = len(queue)
        for _ in range(size):
            combo = queue.popleft()
            for letter in mapping[digit]:
                queue.append(combo + letter)

    return list(queue)


# Q4: Using itertools.product
def letterCombinations_product(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: Use itertools.product for Cartesian product.
    """
    if not digits:
        return []

    from itertools import product

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    digit_letters = [mapping[d] for d in digits]
    return [''.join(combo) for combo in product(*digit_letters)]


# Q5: DFS with helper function
def letterCombinations_dfs(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: DFS with explicit helper function.
    """
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def dfs(index):
        if index == len(digits):
            return ['']

        result = []
        for letter in mapping[digits[index]]:
            for combo in dfs(index + 1):
                result.append(letter + combo)

        return result

    return dfs(0)


# Q6: List comprehension
def letterCombinations_listcomp(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: Use list comprehension for concise code.
    """
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = ['']
    for digit in digits:
        result = [combo + letter for combo in result for letter in mapping[digit]]

    return result


# Q7: Recursive with list building
def letterCombinations_recursive_list(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: Recursive approach with explicit list building.
    """
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def combine(index):
        if index == len(digits):
            return ['']

        rest = combine(index + 1)
        result = []

        for letter in mapping[digits[index]]:
            for combo in rest:
                result.append(letter + combo)

        return result

    return combine(0)


# Q8: Generator approach
def letterCombinations_generator(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: Use generators for lazy evaluation.
    """
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def gen_combinations(index, current):
        if index == len(digits):
            yield current
        else:
            for letter in mapping[digits[index]]:
                yield from gen_combinations(index + 1, current + letter)

    return list(gen_combinations(0, ''))


# Q9: Dictionary mapping with recursion
def letterCombinations_dict_recursive(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: Dictionary-based mapping with recursion.
    """
    if not digits:
        return []

    phone_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def helper(index, path):
        if index == len(digits):
            return [path]

        result = []
        for letter in phone_map[digits[index]]:
            result.extend(helper(index + 1, path + letter))

        return result

    return helper(0, '')


# Q10: Tail recursion approach
def letterCombinations_tail_recursive(digits: str) -> list[str]:
    """
    Time Complexity: O(4^n)
    Space Complexity: O(4^n)

    Approach: Tail recursive approach with accumulator.
    """
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def tail_rec(index, accumulator):
        if index == len(digits):
            return accumulator

        new_accumulator = []
        for combo in accumulator:
            for letter in mapping[digits[index]]:
                new_accumulator.append(combo + letter)

        return tail_rec(index + 1, new_accumulator)

    return tail_rec(0, [''])


if __name__ == "__main__":
    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
        ("234", ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
                 "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
                 "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]),
        ("2345", ["adgj", "adgk", "adgl", "adhj", "adhk", "adhl", "adij", "adik", "adil",
                  "aegj", "aegk", "aegl", "aehj", "aehk", "aehl", "aeij", "aeik", "aeil",
                  "afgj", "afgk", "afgl", "afhj", "afhk", "afhl", "afij", "afik", "afil",
                  "bdgj", "bdgk", "bdgl", "bdhj", "bdhk", "bdhl", "bdij", "bdik", "bdil",
                  "begj", "begk", "begl", "behj", "behk", "behl", "beij", "beik", "beil",
                  "bfgj", "bfgk", "bfgl", "bfhj", "bfhk", "bfhl", "bfij", "bfik", "bfil",
                  "cdgj", "cdgk", "cdgl", "cdhj", "cdhk", "cdhl", "cdij", "cdik", "cdil",
                  "cegj", "cegk", "cegl", "cehj", "cehk", "cehl", "ceij", "ceik", "ceil",
                  "cfgj", "cfgk", "cfgl", "cfhj", "cfhk", "cfhl", "cfij", "cfik", "cfil"]),
        ("42", ["ga", "gb", "gc", "ha", "hb", "hc", "ia", "ib", "ic"]),
    ]

    functions = [
        letterCombinations_backtrack,
        letterCombinations_iterative,
        letterCombinations_bfs,
        letterCombinations_product,
        letterCombinations_dfs,
        letterCombinations_listcomp,
        letterCombinations_recursive_list,
        letterCombinations_generator,
        letterCombinations_dict_recursive,
        letterCombinations_tail_recursive,
    ]

    for i, func in enumerate(functions, 1):
        print(f"\nQ{i}: {func.__name__}")
        print("-" * 70)
        all_passed = True
        for digits, expected in test_cases:
            result = func(digits)
            result.sort()
            expected.sort()
            passed = result == expected
            all_passed = all_passed and passed
            status = "✓" if passed else "✗"
            display_result = result if len(result) <= 5 else result[:5] + ["..."]
            print(f"  {status} letterCombinations('{digits}') = {display_result} (length: {len(result)})")

        if all_passed:
            print(f"  All tests passed!")
