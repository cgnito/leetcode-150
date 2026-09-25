# 169. Majority Element

## Problem

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than `⌊n / 2⌋` times**.

You may assume that the majority element always exists in the array.

The follow-up asks for:

```text
Time:  O(n)
Space: O(1)
```

---

## Approach 1 — Hash Map

### Mental Model

Count how many times each number appears.

```text
nums = [2, 2, 1, 1, 1, 2, 2]

2 → 4
1 → 3
```

Loop through the array and update the count:

```python
counts[num] = counts.get(num, 0) + 1
```

If we've never seen `num`:

```text
counts.get(num, 0) → 0
```

so it becomes `1`.

If we've seen it before, its existing count is incremented.

After counting everything, return the number with the largest count:

```python
max(counts, key=counts.get)
```

### Implementation

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        return max(counts, key=counts.get)
```

### Complexity

* **Time:** O(n)
* **Space:** O(n)

The hash map can store up to `n` different values.

---

# Approach 2 — Boyer-Moore Voting Algorithm

The important thing here is understanding **why we can cancel elements**.

The problem guarantees that the majority element appears **more than half of the array**:

```text
majority > n / 2
```

That means all the other elements combined occur **less than half** of the array.

So even if we pair a majority element with a different element and **cancel them out**, there will still be majority elements left.

### Mental Model

Think of the array as a fight between the current candidate and everything that disagrees with it.

```text
same as candidate  → +1
different           → -1
```

When `count` reaches `0`, the previous candidate has been completely cancelled out, so we choose the next number as the new candidate.

```text
candidate = None
count = 0
```

For every number:

```text
count == 0
    ↓
choose current number as candidate

same as candidate
    ↓
count += 1

different from candidate
    ↓
count -= 1
```

---

## The Cancellation Idea

Example:

```text
[2, 2, 1, 1, 1, 2, 2]
```

Start:

```text
candidate = 2
count = 1
```

Another `2` supports the candidate:

```text
2 → count = 2
```

A `1` disagrees:

```text
1 → count = 1
```

Another `1` disagrees:

```text
1 → count = 0
```

The two `2`s and two `1`s have effectively cancelled each other:

```text
2 + 2
1 + 1
──────
cancelled
```

Now the next `2` becomes the new candidate.

The important part is:

> **The majority element occurs more than all the other elements combined, so after cancellation, the majority element must remain.**

---

## Implementation

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1

        return candidate
```

---

## Why This Works

`count` represents the **net support** for the current candidate.

```text
same value       → +1
different value  → -1
```

Every `-1` can cancel one `+1`.

Since the majority element appears more than `n / 2` times, there aren't enough non-majority elements to cancel all of its occurrences.

Therefore, after all the cancellation:

```text
majority elements > other elements
```

and the majority element remains as the candidate.

---

## Pattern to Remember

When you see:

> **An element appears more than half of the array**

Think:

```text
majority > n / 2
        ↓
majority > everything else combined
        ↓
pair/cancel different elements
        ↓
majority must survive
        ↓
Boyer-Moore Voting Algorithm
```

### One-line memory

> **The majority element appears more than all other elements combined, so cancel different elements against each other; the majority survives.**

---

## Complexity

### Hash Map

```text
Time:  O(n)
Space: O(n)
```

### Boyer-Moore

```text
Time:  O(n)
Space: O(1)
```

Boyer-Moore only keeps two pieces of information:

```text
candidate
count
```
