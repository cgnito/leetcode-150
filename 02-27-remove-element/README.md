# 27. Remove Element

## Problem

Given an array `nums` and a value `val`, remove every occurrence of `val` **in-place**.

We don't actually need to shrink the array.

We only need to make sure that:

```text
nums[0:k]
```

contains all the elements that are **not equal to `val`**, and return `k`.

The elements after `k` don't matter.

---

## Intuition

When I see:

> **remove/filter elements from an array in-place**

I think:

> **scan the array and move the elements I want to keep toward the front.**

I don't need another array.

I can use two pointers:

```text
read  → scans the entire array
write → tells me where the next valid element should go
```

### Mental picture

```text
nums = [0, 1, 2, 2, 3, 0, 4, 2]
        ↑
      write

        ↑
       read
```

`read` explores the array.

`write` builds the portion of the array that we want to keep.

---

## The Rule

For every element that `read` sees:

### If it is `val`

Ignore it.

```text
nums[read] == val
        ↓
      skip
```

### If it is NOT `val`

Copy it to the `write` position:

```text
nums[read] != val
        ↓
nums[write] = nums[read]
        ↓
write++
```

This gives us the invariant:

> **Everything before `write` is already a valid element that should remain in the array.**

---

## Example

```text
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
```

Initially:

```text
write
  ↓
[0, 1, 2, 2, 3, 0, 4, 2]
  ↑
 read
```

### `read = 0`

`0 != 2`, so keep it.

```text
nums[write] = nums[read]
```

```text
[0, 1, 2, 2, 3, 0, 4, 2]
 ↑
write
```

Then `write++`.

---

### `read = 1`

`1 != 2`, so keep it.

```text
[0, 1, 2, 2, 3, 0, 4, 2]
    ↑
  write
```

---

### `read = 2`

```text
nums[read] == 2
```

This is the value we're removing.

Skip it.

`write` does **not** move.

---

### `read = 3`

Again:

```text
nums[read] == 2
```

Skip it.

`write` still doesn't move.

---

### `read = 4`

`3 != 2`.

Put it at `write`:

```text
[0, 1, 3, 2, 3, 0, 4, 2]
       ↑
     write
```

The old value at that position doesn't matter anymore because we're building the valid prefix.

Continue this process until `read` reaches the end.

Final relevant portion:

```text
[0, 1, 3, 0, 4, _, _, _]
             ↑
             k
```

`write == 5`, so return:

```python
return write
```

The first `5` elements are the answer.

---

## Implementation

```python
class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:

        write = 0

        for read in range(len(nums)):

            if nums[read] == val:
                continue

            nums[write] = nums[read]
            write += 1

        return write
```

---

## Why We Don't Actually Remove Anything

A common mistake is thinking we need to physically delete the elements.

We don't.

The problem only cares about:

```text
nums[0:k]
```

So if we have:

```text
[0, 1, 3, 0, 4, 2, 2, 2]
              ↑
              k
```

only this matters:

```text
[0, 1, 3, 0, 4]
```

Everything after `k` is irrelevant.

This is why we can simply **overwrite the array from the front**.

---

## Pattern to Remember

When I see:

> **remove/filter certain elements in-place**

Think:

```text
two pointers
    ↓
read  = scan everything
write = position for next valid element
    ↓
if nums[read] is valid:
    nums[write] = nums[read]
    write++
    ↓
return write
```

### One-line memory

> **Read everything, keep the valid elements, compact them toward the front.**

---

## Complexity

```text
Time:  O(n)
Space: O(1)
```

We scan the array once and use only two pointers.
