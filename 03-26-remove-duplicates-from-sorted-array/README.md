# 26. Remove Duplicates from Sorted Array

## Problem

Given a **sorted** array, remove duplicates **in-place** so that each value appears only once.

Return `k`, the number of unique elements.

Only the first `k` elements matter.

---

## Intuition

The most important thing to notice is:

> **The array is already sorted.**

Because it is sorted, duplicates will always be **next to each other**.

```text
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
 ↑  ↑
same value → duplicate
```

I only need to ask:

> **"Is the current value different from the previous value?"**

If it is different, it is a new unique value.

---

## Read / Write Pattern

This is the same **read/write pointer** pattern as `Remove Element`.

```text
read  → scans the array
write → position where the next unique value goes
```


```text
if current != previous:
    keep it
```

---

## Why Start `write = 1`?

The first element is automatically unique.

For example:

```text
[1, 1, 2, 3]
 ↑
unique
```

So we can immediately consider the first element part of our answer.

```text
write = 1
read = 1
```

`write` represents the position where the **next unique element** should be placed.

---

## Algorithm

Start from the second element.

For every `read`:

```text
nums[read] == nums[read - 1]
        ↓
    duplicate
        ↓
      skip
```

If they are different:

```text
nums[read] != nums[read - 1]
        ↓
    new unique value
        ↓
nums[write] = nums[read]
        ↓
     write++
```

### Visual

```text
nums = [0, 0, 1, 1, 2, 2, 3]

        read
          ↓
[0, 0, 1, 1, 2, 2, 3]
 ↑
write
```

`0 == 0` → duplicate → skip.

Then:

```text
          read
            ↓
[0, 0, 1, 1, 2, 2, 3]
    ↑
  write
```

`1 != 0` → new value.

Put `1` at `write`:

```text
[0, 1, 1, 1, 2, 2, 3]
       ↑
     write
```

Continue until the end.

Result:

```text
[0, 1, 2, 3, _, _, _]
          ↑
        k = 4
```

Return `write`.

---

## Implementation

```python
class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:

        write = 1

        for read in range(1, len(nums)):

            if nums[read] == nums[read - 1]:
                continue

            nums[write] = nums[read]
            write += 1

        return write
```

---

## Why This Works

Because the array is sorted, all occurrences of the same value are adjacent.

Therefore:

```text
current == previous
```

means the current value is a duplicate.

And:

```text
current != previous
```

means we found a new unique value.

The portion before `write` always contains the unique values we've found so far.

```text
[ unique | unique | unique | ... | untouched ]
                    ↑
                  write
```

---

## Pattern to Remember

When I see:

> **sorted array + remove duplicates + in-place**

Immediately think:

```text
sorted
  ↓
duplicates are adjacent
  ↓
read/write pointers
  ↓
compare current with previous
  ↓
different → write it
same → skip it
```

### One-line memory

> **Sorted array means duplicates are adjacent, so scan once and compact only when the value changes.**

---

## Complexity

**Time:** `O(n)`

Each element is visited exactly once.

**Space:** `O(1)`

Only the `read` and `write` pointers are used.
