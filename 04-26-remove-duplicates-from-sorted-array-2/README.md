# 80. Remove Duplicates from Sorted Array II

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** so that each unique element appears **at most twice**.

The relative order must remain the same.

Return `k`, where the first `k` elements of `nums` contain the final result.

You must modify the array in-place with **O(1) extra memory**.

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
if invalid:
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

Each number can appear at most twice.

Because the array is sorted, if the current number equals the number **two positions behind `write`**, we've already kept two copies:

```python
nums[read] == nums[write - 2]
```

So skip it.

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0

        for read in range(len(nums)):
            if write >= 2 and nums[read] == nums[write - 2]:
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
