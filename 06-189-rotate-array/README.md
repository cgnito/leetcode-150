# Rotate Array

## Problem

Given an array `nums`, rotate it to the right by `k` steps.

The rotation must modify the input array.

---

## Intuition

My first approach was:

```python
for _ in range(k):
    nums.insert(0, nums.pop())
```

This works, but it is too slow.

Each `insert(0, ...)` shifts the existing elements, so one rotation costs `O(n)`. Doing that `k` times gives roughly:

```text
O(n × k)
```

Instead, notice that rotating by `n` positions brings the array back to its original state.

So we only need:

```python
k %= n
```

Then the rotated array can be built as:

```python
nums[-k:] + nums[:-k]
```

---

## Key Points

### 1. Reduce unnecessary rotations

For:

```text
nums = [1,2,3,4,5]
k = 7
```

Since:

```text
7 % 5 = 2
```

rotating 7 times is the same as rotating 2 times.

```text
[1,2,3,4,5]
       ↓ rotate 2
[4,5,1,2,3]
```

### 2. `nums[:]` modifies the original list

This:

```python
nums = nums[-k:] + nums[:-k]
```

creates a new list and makes `nums` point to it.

But:

```python
nums[:] = nums[-k:] + nums[:-k]
```

replaces the contents of the **existing list**.

```text
nums
 ↓
[1,2,3,4,5]

        nums[:] =
              ↓
[4,5,1,2,3]
```

So the original list object is modified.

**Note:** the slicing still creates new lists, so this approach uses `O(n)` extra space.

---

## Implementation

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)

        nums[:] = nums[-k:] + nums[:-k]
```

---

## Pattern Recognition

When you see:

* rotate an array
* `k` can be very large
* modify the array in-place

Think:

```text
rotation
   ↓
k % n
   ↓
split at n-k
   ↓
move the last k elements to the front
```

For the basic approach:

> **Array rotation → reduce `k` with `% n`, then split the array into the part that moves and the part that stays.**

The O(1)-space follow-up uses the **reversal pattern**.
