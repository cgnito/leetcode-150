# Best Time to Buy and Sell Stock

## Problem

Given an array `prices` where `prices[i]` is the stock price on day `i`, choose **one day to buy** and a **different future day to sell** to maximize profit.

Return the maximum profit. If no profit is possible, return `0`.

---

## Translate the Problem

Don't think:

> "Find the lowest price in the whole array, then find the highest price after it."

Instead, translate the problem to:

> **"If I sell today, what is the cheapest price I could have bought at before today?"**

For every price:

```text
cheapest buy seen so far
            ↓
       current price
            ↓
    profit if I sell today
```

Then keep the **best profit seen so far**.

This automatically guarantees that the buy happens before the sell.

---

## Intuition

As I scan from left to right, I only need to remember two things:

```text
buy     → cheapest price seen so far
profit  → maximum profit seen so far
```

If I find a cheaper price:

```python
buy = prices[i]
```

because a cheaper buy is always better for every future selling day.

Then:

```python
prices[i] - buy
```

is the profit if I sell today.

If that profit is better than my current `profit`, update it.

### Mental Model

```text
Scan → remember cheapest buy → calculate today's profit → keep the best
```

---

## Approach

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            if prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit
```

### Why it works

A cheaper price makes every **future** sale potentially more profitable, so we can safely forget the previous, more expensive buy price.

We never need to check every pair.

---

## Pattern Recognition

Look for problems where:

* you're scanning left → right
* the current element is combined with something from the past
* you need the **best/minimum/maximum previous value**
* you can discard worse previous candidates

Think:

> **Running minimum/maximum + greedy**

For this problem:

```text
Previous values → minimum so far
Current value   → calculate result
Result          → maximum so far
```

**Complexity:** `O(n)` time, `O(1)` space.
