# Best Time to Buy and Sell Stock II

## Problem

You are given an integer array prices where prices\[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

---

## Translate the Problem

Instead of thinking:

> "Where should I buy and where should I sell?"

Translate it to:

> **"For every day-to-day price increase, can I capture that increase as profit?"**

Yes.

Since I can make multiple transactions, I don't need to find one perfect buy/sell pair. I can capture **every profitable upward movement**.

---

## Intuition

Look at each pair of consecutive days:

```text
[7, 1, 5, 3, 6, 4]

7 → 1   -6   ❌
1 → 5   +4   ✅
5 → 3   -2   ❌
3 → 6   +3   ✅
6 → 4   -2   ❌
```

Only add the positive differences:

```text
4 + 3 = 7
```

This is equivalent to:

```text
(5 - 1) + (6 - 3) = 7
```

For continuously increasing prices:

```text
[1, 2, 3, 4, 5]

(2-1) + (3-2) + (4-3) + (5-4)
= 4
```

which is the same profit as buying at `1` and selling at `5`.

---

## Approach

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
```

Mental model:

```text
current > previous?
       ↓
     yes → collect the difference
     no  → ignore it
```

---

## Pattern Recognition

This is a **greedy + local difference** pattern.

When you see:

* multiple transactions are allowed
* you can only hold one at a time
* maximize total profit
* no transaction fee/cooldown

Think:

> **"Capture every positive increase."**

### #121 vs #122

```text
#121: ONE transaction
      → running minimum + maximum profit

#122: UNLIMITED transactions
      → add every positive difference
```

**Complexity:** `O(n)` time, `O(1)` space.
