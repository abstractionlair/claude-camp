# Pattern Reference Guide

## Core Patterns for Technical Interviews

### 1. Two Pointers
**Recognition Triggers:**
- Sorted array or linked list
- Finding pairs with specific sum/difference
- Removing duplicates in-place
- Palindrome checking

**Key Insight:** Move pointers based on comparison to target

**Common Mistakes:**
- Forgetting to handle duplicates
- Off-by-one errors with pointer bounds

---

### 2. Sliding Window
**Recognition Triggers:**
- Substring/subarray problems
- "Maximum/minimum length" with condition
- "At most k" constraints
- Continuous elements

**Fixed vs Variable:**
- Fixed: Window size given (e.g., "max sum of k elements")
- Variable: Find optimal size (e.g., "longest substring with k distinct")

**Key Insight:** Maintain window invariant, expand right, shrink left

---

### 3. Binary Search
**Recognition Triggers:**
- Sorted array
- Finding specific value or insertion point
- "Minimum/maximum value such that..."
- Search space reduction

**Variations:**
- Classic: Find exact value
- Lower bound: First occurrence or insertion point
- Upper bound: Last occurrence
- Search on answer: Binary search the solution space

**Stdlib:** Use `bisect.bisect_left()` and `bisect.bisect_right()`

---

### 4. DFS/BFS
**Recognition Triggers:**
- Tree/graph traversal
- Finding paths
- Connected components
- "All possible" solutions

**When to use which:**
- BFS: Shortest path (unweighted), level-order
- DFS: Path exists, exhaustive search, less memory

**Implementation:**
- BFS: Use `collections.deque()`
- DFS: Recursion or stack

---

### 5. Dynamic Programming
**Recognition Triggers:**
- "Number of ways"
- "Minimum/maximum cost"
- Optimal substructure
- Overlapping subproblems
- Choices at each step

**Approach:**
1. Define state (what parameters uniquely identify subproblem)
2. Write recurrence relation
3. Identify base cases
4. Decide iteration order (bottom-up) or use memoization (top-down)

---

### 6. Heap/Priority Queue
**Recognition Triggers:**
- K largest/smallest elements
- Running median
- Merge K sorted lists
- Task scheduling

**Stdlib:** `heapq` (min-heap by default!)
- For max-heap: negate values
- `heappush()`, `heappop()`, `heapify()`

---

### 7. Monotonic Stack
**Recognition Triggers:**
- Next greater/smaller element
- Largest rectangle in histogram
- Stock span problems
- Temperature/building visibility

**Key Insight:** Maintain elements in increasing/decreasing order

---

### 8. Union-Find (Disjoint Set)
**Recognition Triggers:**
- Connected components
- Detect cycles in undirected graph
- Minimum spanning tree
- Account merging problems

**Operations:** 
- Find with path compression
- Union by rank/size

---

### 9. Topological Sort
**Recognition Triggers:**
- Dependencies between tasks
- Course prerequisites
- Build order
- Directed acyclic graph (DAG)

**Approaches:**
- DFS with finish times
- Kahn's algorithm (BFS with in-degrees)

---

### 10. Backtracking
**Recognition Triggers:**
- Generate all combinations/permutations
- N-queens, Sudoku
- Path finding with constraints
- "All valid" solutions

**Template:**
```python
def backtrack(state):
    if is_solution(state):
        record_solution(state)
        return
    
    for choice in get_choices(state):
        if is_valid(choice):
            make_choice(choice)
            backtrack(state)
            undo_choice(choice)
```

---

## Quick Decision Tree

1. **Array problem?**
   - Sorted? → Binary search, Two pointers
   - Subarray? → Sliding window, Prefix sum
   - Pairs/triplets? → Two pointers, Hash map

2. **String problem?**
   - Substring? → Sliding window
   - Palindrome? → Two pointers, DP
   - Pattern matching? → KMP, Rolling hash

3. **Tree/Graph?**
   - Shortest path? → BFS (unweighted), Dijkstra (weighted)
   - All paths? → DFS/Backtracking
   - Detect cycle? → DFS (directed), Union-Find (undirected)

4. **Optimization?**
   - Choices at each step? → DP or Greedy
   - Generate all? → Backtracking
   - K best elements? → Heap

5. **Design/Data structure?**
   - LRU/LFU? → OrderedDict, Double linked list
   - Median stream? → Two heaps
   - Range queries? → Segment tree, Fenwick tree
