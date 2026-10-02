# Jump Game II

## Problem

Given an integer array `nums`, you start at index `0`.

Each `nums[i]` represents the **maximum number of positions you can jump forward from index `i`**.

Return the **minimum number of jumps** needed to reach the last index.

It is guaranteed that the last index is reachable.

Example:

```text
[2, 3, 1, 1, 4]

0 → 1 → 4

Minimum jumps = 2
```

---

## Translate the Problem

Jump Game I (#55) asked:

> **"Can I reach the end?"**

Jump Game II asks:

> **"How many jumps do I need to reach the end?"**

The key is to think about **ranges rather than individual jumps**.

Instead of choosing an exact jump immediately, think:

> **"With my current number of jumps, what range of indices can I reach?"**

Then:

> **"While I'm inside that range, what is the furthest position I could reach with one more jump?"**

When I've finished exploring the current range, I must make another jump.

---

## Intuition

Consider:

```text
[2, 3, 1, 1, 4]
 0  1  2  3  4
```

From index `0`:

```text
nums[0] = 2
```

With one jump, I can reach:

```text
index 1
index 2
```

So my current range is:

```text
[2, 3, 1, 1, 4]
 0 [1  2] 3  4
    └────┘
  current range
```

I now examine the positions inside that range.

### Index 1

```text
1 + nums[1]
1 + 3
= 4
```

Index `1` could take me to `4`.

### Index 2

```text
2 + nums[2]
2 + 1
= 3
```

Index `2` can only take me to `3`.

Therefore, the best possible next reach is:

```text
furthest = 4
```

Once I've finished examining the current range, I count another jump.

```text
jumps = 2
```

And `4` is the destination.

---

## The Important Insight

The mistake to avoid is thinking:

> "I need to immediately choose the index with the biggest jump."

Instead:

> **"I need to examine everything reachable with my current number of jumps, and find how far the next jump could take me."**

We're not really choosing a specific path while scanning.

We're calculating the **best possible boundary for the next jump**.

---

## Two Boundaries

This problem becomes much easier once you understand that we need two different boundaries.

### `current_end`

```text
current_end = end of the range reachable with the current number of jumps
```

It answers:

> **"How far can I currently get without taking another jump?"**

### `furthest`

```text
furthest = furthest position I can reach from the positions I'm currently examining
```

It answers:

> **"If I take one more jump, how far could I get?"**

So:

```text
current_end
     ↓
[positions I can reach with current jumps]
                ↓
             examine
                ↓
          find furthest
                ↓
       take another jump
                ↓
        current_end = furthest
```

---

## Example Step-by-Step

For:

```text
[2, 3, 1, 1, 4]
```

Initially:

```text
jumps = 0
current_end = 0
furthest = 0
```

### Examine index 0

```text
i = 0
nums[0] = 2

furthest = max(0, 0 + 2)
         = 2
```

We've reached the end of the current range:

```text
i == current_end
0 == 0
```

So we need another jump:

```text
jumps = 1
current_end = 2
```

Our new current range is:

```text
[2, 3, 1, 1, 4]
 0 [1  2] 3  4
    └────┘
 current_end
```

### Examine index 1

```text
furthest = max(2, 1 + 3)
         = 4
```

### Examine index 2

```text
furthest = max(4, 2 + 1)
         = 4
```

We've now reached the end of the current range:

```text
i == current_end
2 == 2
```

So:

```text
jumps = 2
current_end = 4
```

We've reached the destination.

---

## Why `i == current_end` Matters

This is the most important line in the solution:

```python
if i == current_end:
```

It means:

> **"I've finished examining every position that was reachable with my current number of jumps."**

Therefore, if I still haven't reached the destination, I need another jump.

So:

```python
jumps += 1
current_end = furthest
```

means:

> "Take another jump, and the new range ends at the furthest position I discovered."

---

## Why We Don't Increment `jumps` When We Find `furthest`

Suppose:

```text
[2, 3, 1, 1, 4]
```

From `0`, I can reach `1` and `2`.

While examining them:

```text
1 → 4
2 → 3
```

Finding that `1` can reach `4` doesn't immediately mean:

```text
jumps += 1
```

We're still exploring the range belonging to the current jump.

Only when we've reached:

```text
i == current_end
```

have we exhausted that range.

That's when we commit to the next jump.

---

## Approach

1. `current_end` tracks the end of the range reachable with the current number of jumps.
2. `furthest` tracks the furthest position that the next jump could reach.
3. Scan through the current range.
4. For each index, calculate:

   ```python
   i + nums[i]
   ```

   and update `furthest`.
5. When `i == current_end`, the current range is exhausted.
6. Increment `jumps`.
7. Set:

   ```python
   current_end = furthest
   ```
8. Continue until the last index.

Because the problem guarantees that the last index is reachable, we don't need to handle an impossible case.

---

## Implementation

```python
class Solution:
    def jump(self, nums: list[int]) -> int:
        furthest = 0
        jumps = 0
        current_end = 0

        for i in range(len(nums) - 1):
            furthest = max(furthest, nums[i] + i)

            if i == current_end:
                jumps += 1
                current_end = furthest

        return jumps
```

---

## Why It Works

Every `current_end` represents the furthest position reachable using the current number of jumps.

While scanning that range, `furthest` finds the best possible boundary for the next jump.

When the scan reaches `current_end`, we've considered every option available with the current number of jumps.

Therefore, extending to `furthest` gives us the best possible range for the next jump.

This is greedy because we always maximize the reachable boundary rather than exploring individual jump sequences.

---

## Pattern Recognition

### Greedy Range Expansion

This problem is essentially **Jump Game I + counting the ranges**.

### #55

Question:

> **"Can I reach the end?"**

Track:

```text
max_reach
```

Meaning:

> Furthest position I can currently reach.

### #45

Question:

> **"How many jumps are needed to reach the end?"**

Track:

```text
current_end
```

Meaning:

> End of the range reachable with the current number of jumps.

And:

```text
furthest
```

Meaning:

> Furthest boundary the next jump could reach.

Mental model:

```text
CURRENT RANGE
      ↓
[  reachable positions  ]
             ↓
       scan everything
             ↓
     find furthest reach
             ↓
       range exhausted
             ↓
        jumps += 1
             ↓
   current_end = furthest
```

### One-line memory

> **"Scan the current reachable range, find the furthest next range, then count a jump when the current range ends."**

---

## Complexity

* **Time:** `O(n)` — every index is scanned at most once.
* **Space:** `O(1)` — only a few variables are maintained.
