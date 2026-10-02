# Jump Game

## Problem

Given an integer array `nums`, you start at index `0`.

Each `nums[i]` represents the **maximum number of positions you can jump forward from index `i`**.

Return `True` if you can reach the last index, otherwise return `False`.

Example:

```text
[2, 3, 1, 1, 4]

0 → can reach 1 or 2
1 → can reach 2, 3, or 4

Therefore → True
```

---

## Translate the Problem

Don't think:

> "What exact jumps should I make?"

Instead, translate the problem to:

> **"As I move through the array, what is the furthest index I can currently reach?"**

At every reachable index, I can potentially extend my reachable range.

So I only need to maintain:

```text
max_reach = furthest index I can currently reach
```

---

## Intuition

Consider:

```text
[2, 3, 1, 1, 4]
 0  1  2  3  4
```

Start at index `0`.

```text
nums[0] = 2
```

So from index `0`, I can reach index `2`.

```text
max_reach = 2
```

Now index `1` is inside that reachable range, so I can examine it.

```text
index 1
nums[1] = 3

1 + 3 = 4
```

Now my reachable range extends to index `4`.

```text
max_reach = 4
```

Since `4` is the last index, I can reach the end.

---

## The Important Idea: Reachable Boundary

Think of `max_reach` as a boundary:

```text
[2, 3, 1, 1, 4]
 0  1  2  3  4
 └────────────┘
      ↑
  max_reach
```

Everything at or before `max_reach` is potentially reachable.

If I ever encounter:

```python
i > max_reach
```

then I've reached an index that I **cannot get to**.

Therefore:

```python
return False
```

For example:

```text
[3, 2, 1, 0, 4]
 0  1  2  3  4
 └─────────┘
 max_reach = 3
```

When `i = 4`:

```text
4 > 3
```

Index `4` is unreachable, so the answer is `False`.

---

## The Key Calculation

Whenever an index is reachable, ask:

> **"If I use this index, how far could I reach?"**

That's:

```python
i + nums[i]
```

But I don't necessarily want to replace my existing reach with that value.

I want whichever is larger:

```python
max_reach = max(max_reach, i + nums[i])
```

So:

```text
current reachable boundary
        ↓
max_reach

potential new boundary
        ↓
i + nums[i]

keep the larger one
```

---

## Important Edge Case

Consider:

```text
[0]
```

There is only one index.

We're already standing on the last index, so the answer is `True`.

The important realization is:

> **You don't need to make a jump if you're already at the destination.**

---

## Approach

1. Start `max_reach` at the first index's maximum reach.
2. Scan the array from left to right.
3. If `i > max_reach`, the current index cannot be reached → return `False`.
4. Otherwise, calculate how far the current index could reach:

   ```python
   i + nums[i]
   ```
5. Update `max_reach` if this extends the reachable boundary.
6. If `max_reach` reaches the last index, return `True`.
7. If the loop finishes without getting stuck, return `True`.

---

## Implementation

```python
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = nums[0]

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, nums[i] + i)

            if max_reach >= len(nums) - 1:
                return True

        return True
```

---

## Why It Works

The algorithm doesn't try every possible sequence of jumps.

Instead, it continuously maintains the **furthest position that can be reached using any valid path discovered so far**.

If an index is within `max_reach`, it is reachable and can potentially extend the range.

If an index is beyond `max_reach`, there is no way to reach it, so the last index cannot be reached either.

---

## Pattern Recognition

### Greedy + Running Maximum + Reachability

When you see a problem involving:

* positions/indices
* each position gives you some amount of reach
* "can I reach the end?"
* maximum jump/movement
* possible dead ends

Think:

> **"Can I maintain the furthest reachable position?"**

Mental model:

```text
reachable position
        ↓
    max_reach
        ↓
Can the current position extend it?
```

This is a **greedy** approach because we don't need to explore every possible jump. We only care about the best/furthest reachable boundary.

### One-line memory

> **"Scan reachable positions and keep extending the furthest boundary."**

---

## Complexity

* **Time:** `O(n)` — each index is visited once.
* **Space:** `O(1)` — only `max_reach` is maintained.
