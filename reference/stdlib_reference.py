# Python Standard Library Quick Reference

## Collections Module

### Counter
```python
from collections import Counter

# Create and use
counter = Counter(iterable)  # Count elements
counter = Counter()  # Empty counter
counter['key'] += 1  # Increment

# Useful methods
counter.most_common(k)  # Top k elements as [(elem, count)]
counter.update(iterable)  # Add counts
counter.subtract(iterable)  # Subtract counts

# Get unique elements count
len(counter)  # Number of unique elements
sum(counter.values())  # Total count
```

### defaultdict
```python
from collections import defaultdict

# Common patterns
dd = defaultdict(list)  # NOT defaultdict([])
dd = defaultdict(int)   # Defaults to 0
dd = defaultdict(set)   # Empty set default

# Graph adjacency list
graph = defaultdict(list)
graph[node].append(neighbor)
```

### deque
```python
from collections import deque

# Double-ended queue - O(1) operations both ends
dq = deque()
dq.append(x)      # Add right
dq.appendleft(x)  # Add left
dq.pop()          # Remove right
dq.popleft()      # Remove left

# Use for BFS
queue = deque([start_node])
while queue:
    node = queue.popleft()
```

## Heap Operations (heapq)

```python
import heapq

# MIN-HEAP by default!
heap = []
heapq.heappush(heap, val)  # Add element
min_val = heapq.heappop(heap)  # Remove minimum

# Convert list to heap in-place
heapq.heapify(nums)  # O(n)

# For MAX-HEAP: negate values
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)

# K largest/smallest
heapq.nlargest(k, iterable)  # K largest
heapq.nsmallest(k, iterable)  # K smallest

# Merge sorted iterables
merged = heapq.merge(sorted1, sorted2)
```

## Binary Search (bisect)

```python
import bisect

# Find insertion points in sorted array
bisect.bisect_left(arr, x)   # Leftmost position
bisect.bisect_right(arr, x)  # Rightmost position
bisect.bisect(arr, x)         # Same as bisect_right

# Insert maintaining sort
bisect.insort_left(arr, x)   # Insert at leftmost valid position
bisect.insort_right(arr, x)  # Insert at rightmost valid position

# Common patterns
def binary_search(arr, target):
    pos = bisect.bisect_left(arr, target)
    return pos < len(arr) and arr[pos] == target

def count_less_than(arr, val):
    return bisect.bisect_left(arr, val)
```

## Itertools

```python
import itertools

# Combinatorics
itertools.combinations(iterable, r)     # nCr combinations
itertools.permutations(iterable, r)     # nPr permutations
itertools.product(iter1, iter2)        # Cartesian product

# Useful utilities
itertools.accumulate(iterable)         # Running sum/product
itertools.chain(iter1, iter2)         # Concatenate iterables
itertools.groupby(iterable, key=func) # Group consecutive elements

# Example: all pairs
pairs = itertools.combinations(arr, 2)

# Example: running sum
prefix_sums = list(itertools.accumulate(nums))
```

## Other Useful Built-ins

### Math
```python
import math

math.inf   # Positive infinity
-math.inf  # Negative infinity
math.gcd(a, b)  # Greatest common divisor
math.lcm(a, b)  # Least common multiple (Python 3.9+)
math.isqrt(n)   # Integer square root (Python 3.8+)
math.comb(n, k) # nCk combinations (Python 3.8+)
```

### String Operations
```python
# Check character types
char.isalpha()   # Letter?
char.isdigit()   # Digit?
char.isalnum()   # Letter or digit?

# ASCII values
ord('a')  # 97
chr(97)   # 'a'

# Case manipulation
s.lower()
s.upper()
s.swapcase()
```

### List/Dict Tricks
```python
# Get with default
dict.get(key, default_value)

# Set default if not exists
dict.setdefault(key, default_value)

# Sort with custom key
arr.sort(key=lambda x: (x[0], -x[1]))  # Sort by first asc, second desc

# Reverse iteration
for i in range(len(arr)-1, -1, -1):
    # Process arr[i]

# Enumerate with start index
for i, val in enumerate(arr, start=1):
    # i starts at 1
```

### Common Gotchas

```python
# WRONG
matrix = [[0] * cols] * rows  # All rows reference same list!

# RIGHT
matrix = [[0] * cols for _ in range(rows)]

# WRONG
default_dict = defaultdict([])  # TypeError!

# RIGHT  
default_dict = defaultdict(list)

# Integer division
5 // 2  # 2 (floor division)
-5 // 2  # -3 (floors toward negative infinity!)

# For ceiling division
import math
math.ceil(5 / 2)  # 3
# Or trick:
(n + k - 1) // k  # Ceiling of n/k
```

## Time Complexity Reminders

- `list.insert(0, x)` - O(n), use `deque.appendleft()` instead
- `x in list` - O(n), use set for O(1)
- `list.pop(0)` - O(n), use `deque.popleft()` instead
- `min(list)`, `max(list)` - O(n) each time, consider heap for repeated operations
- `sorted()` - O(n log n), but `list.sort()` is in-place
- `dict.keys()`, `dict.values()` - O(1) to create view, O(n) to iterate
