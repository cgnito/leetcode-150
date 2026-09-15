# 88. Merge Sorted Array

## Problem

Given two sorted arrays, `nums1` and `nums2`, merge them into `nums1` in sorted order.

`nums1` already has enough empty space at the end to hold all elements from `nums2`.

The important constraints are:

* Both arrays are already sorted.
* We must modify `nums1` **in-place**.
* The first `m` elements of `nums1` are the actual values.
* The last `n` positions are empty space.

---

## Mental Model

When I see:

> **Merge two sorted arrays**

I immediately think:

**Two pointers.**

One pointer for each array:

```text
nums1: [1, 2, 3]
          ↑
          i

nums2: [2, 5, 6]
          ↑
          j
```

Normally, I could compare from the beginning and append the smaller value to a new array.

```text
nums1: [1, 2, 3]
         ↑
         i

nums2: [2, 5, 6]
         ↑
         j

        ↓ compare

result: [1, ...]
```

But this problem requires us to modify `nums1` **in-place**.

If I start writing from the beginning, I can overwrite values in `nums1` that I have not processed yet.

However, `nums1` already has empty space at the **back**.

So instead of merging from the front, I merge from the **back**.

That means I need a third pointer.

---

## The 3 Pointers

```text
nums1 = [1, 2, 3, 0, 0, 0]
          ↑           ↑
          i           k

nums2 = [2, 5, 6]
          ↑
          j
```

### `i`

Points to the last **valid element** in `nums1`.

```python
i = m - 1
```

### `j`

Points to the last element in `nums2`.

```python
j = n - 1
```

### `k`

Points to the last available position in `nums1`.

```python
k = m + n - 1
```

---

## Why Merge From the Back?

`k` is at the end of `nums1`.

Therefore, the largest remaining value should go there.

```text
Compare:

nums1[i]     nums2[j]
    ↓             ↓
    3             6

6 is larger
 ↓

nums1[k] = 6
```

After placing the value:

```text
nums1 = [1, 2, 3, 0, 0, 6]
                    ↑
                    k
```

Then move the pointers backward.

---

## Algorithm

While both arrays still have elements:

1. Compare `nums1[i]` and `nums2[j]`.
2. Take the **larger** value.
3. Put it at `nums1[k]`.
4. Move the pointer belonging to the value we used.
5. Move `k` backward.

```text
                compare
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
 nums1[i] > nums2[j]     nums2[j] >= nums1[i]
        ↓                     ↓
 nums1[k] = nums1[i]     nums1[k] = nums2[j]
        ↓                     ↓
       i--                   j--
        └──────────┬──────────┘
                   ↓
                  k--
```

The main loop is:

```python
while i >= 0 and j >= 0:
```

---

## What About Remaining Elements?

After the main loop, one array may still contain elements.

### Remaining `nums1`

We don't need to do anything.

Why?

Because those elements are already in the correct positions.

### Remaining `nums2`

We **must** copy them into `nums1`.

So:

```python
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1
```

---

## Complete Implementation

```python
class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

---

## Pattern to Remember

When I see:

> **Two sorted arrays + merge + in-place + empty space at the end**

My immediate blueprint should be:

```text
3 pointers
    ↓
i = end of valid nums1
j = end of nums2
k = end of nums1
    ↓
compare i and j
    ↓
take the LARGER
    ↓
put it at k
    ↓
move used pointer
    ↓
k--
    ↓
copy remaining nums2
```

### One-line memory

> **Sorted arrays → two pointers. In-place with space at the back → merge backwards with a third pointer.**

---

## Complexity

**Time:** `O(m + n)`

Every element is processed at most once.

**Space:** `O(1)`

No additional array is created.
