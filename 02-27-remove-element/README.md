# 27. Remove Element

## Problem

Given an array `nums` and a value `val`, remove every occurrence of `val` **in-place**.

Return `k`, where the first `k` elements of `nums` contain all the elements that are **not equal to `val`**.

The elements after `k` don't matter.

You must modify the array **in-place** with **O(1) extra memory**.

---

## Mental Model

### Read scans. Write builds.

```text
read  → scans the entire array
write → marks the boundary of the valid result

[ valid | valid | valid | unwanted | ... ]
                              ↑
                            write
```

The key rule for **in-place modification**:

> **Never allow `write` to move past something that is invalid.**

`read` can keep moving because it is only exploring the array.

If the current element is **invalid**, `continue` immediately:

```python
if nums[read] == val:
    continue
```

This means `write` does not move.

If the current element is **valid**:

```python
nums[write] = nums[read]
write += 1
```

So:

> **`read` explores. `write` only advances when we keep something.**

The unwanted elements don't need to be explicitly deleted. They are eventually **overwritten** by valid elements.

---

## Applying It Here

We want to remove every occurrence of `val`.

So:

```text
nums[read] == val
        ↓
      invalid
        ↓
      skip
```

Otherwise:

```text
nums[read] != val
        ↓
       keep
        ↓
nums[write] = nums[read]
write += 1
```

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

## Complexity

* **Time:** O(n)
* **Space:** O(1)

### Pattern

> **In-place array modification → `read` scans, `write` builds the valid portion. Never let `write` pass an invalid element.**
