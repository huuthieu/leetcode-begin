- **Stack Pattern - Core Concept: Maintaining State/Order Context**
  - Stack acts as memory of "what came before" that matters for current decision
  - Think of it as LIFO history: most recent relevant context is always at the top
  - When iterating through elements, check if current element should interact with stack top
  - Key insight: anything on stack is "unresolved" and waiting for a matching/resolving element

- **Stack Pattern - Specific Applications**
  - **Pair Detection**: save the first element of the pair to the stack, then pop when you encounter the matching second element to validate
    - Examples: matching parentheses/brackets, opening/closing tags
  - **Monotonic Patterns**: keep popping while elements satisfy condition, push current element
    - Examples: next greater element, daily temperatures, largest rectangle
  - **Reverse orders of list/array/...**
  - **Advanced Uses**: undo/redo operations, expression evaluation, path recovery

- **Dynamic Programming Pattern - Core Concept: Optimal Substructure & Overlapping Subproblems**
  - An optimal solution is built from optimal solutions to subproblems
  - The same subproblems are solved multiple times, so we cache results
  - Trade memory for time: avoid recomputing the same states
  - Two approaches: top-down (memoization) or bottom-up (tabulation)

- **Dynamic Programming - When to Use**
  - **Decision Problems**: choosing/rejecting items to maximize/minimize - Examples: coin change, knapsack, house robber
  - **Counting Problems**: count valid combinations/sequences - Examples: climbing stairs, unique paths, decode ways
  - **Optimization Problems**: find max/min value subject to constraints - Examples: longest increasing subsequence, best time to buy/sell stock
  - **String Matching/Transformation**: edit distance, pattern matching with wildcards, palindrome problems
  - **Pattern Recognition**: detect if a string matches a pattern (regex matching, word break)
  - **Interval/Range Problems**: optimal solution depends on how you partition the problem space - Examples: burst balloons, matrix chain multiplication

- **Dynamic Programming - Identifying DP Opportunities**
  - Look for recursive structure: can you define state and transition?
  - Check for overlapping subproblems: will you solve the same state multiple times?
  - Verify optimal substructure: does optimal solution contain optimal solutions to subproblems?
  - Red flags that suggest DP: "count all ways", "maximum/minimum", "find optimal", "can you achieve...", "what's the best..."
  - NOT DP: if each subproblem is independent and solved only once (use greedy or simple recursion)
