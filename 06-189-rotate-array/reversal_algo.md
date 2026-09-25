## Reversal Algorithm

### Intuition

To rotate right by `k`:

```text
[A | B] → [B | A]
```

where `B` is the last `k` elements.

Reverse everything first:

```text
[A | B]
  ↓
[reverse(B) | reverse(A)]
```

Then reverse **B**, then **A**:

```text
[reverse(B) | reverse(A)]
          ↓
[B | A]
```

### Reversing a section

Use two pointers from opposite ends:

```text
left →        ← right
[1  2  3  4  5]
```

Swap them, then move inward:

```python
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```

`left < right` means there are still **two positions to swap**.
Stop when they meet or cross.

### Implementation Blueprint

```text
k %= n

reverse(0, n-1)    # reverse everything
reverse(0, k-1)    # reverse B
reverse(k, n-1)    # reverse A
```

**Memory:** `left/right` → swap → move inward → `left < right`.
