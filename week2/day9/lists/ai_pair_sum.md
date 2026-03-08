# AI Augmented Task — Pair Sum Analysis

## 1. Exact Prompt Used

Write a Python function that finds all pairs in a list that sum to a target number using list comprehensions.

## 2. AI Generated Code

```python
def pair_sum(nums, target):
    return [(nums[i], nums[j]) for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target]

    >>> def pair_sum(nums, target):
...     return [(nums[i], nums[j]) for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == t\arget]
...
>>> print(pair_sum([1, 2, 3, 4, 5], 6))
[(1, 5), (2, 4)]
>>> print(pair_sum([1, 1, 1], 2))
[(1, 1), (1, 1), (1, 1)]
>>> def pair_sum_unique(nums, target):
...     seen = set()
...     pairs = set()
...
...     for num in nums:
...         complement = target - num
...         if complement in seen:
...             pairs.add(tuple(sorted((num, complement))))
...         seen.add(num)
...
...     return sorted(list(pairs))
...
>>> print(pair_sum_unique([1, 2, 3, 4, 5], 6))
... print(pair_sum_unique([1, 1, 1], 2))
... print(pair_sum_unique([2, 4, 3, 3, 5, 1], 6))
...
[(1, 5), (2, 4)]
[(1, 1)]
[(1, 5), (2, 4), (3, 3)]
    