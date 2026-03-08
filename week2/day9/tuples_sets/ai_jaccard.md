# AI Augmented Task — Jaccard Similarity

## 1. Exact Prompt Used

Write a Python function that calculates the Jaccard similarity between two sets of strings. Explain what Jaccard similarity is and where it is used in industry.

## 2. AI Output

```python
def jaccard_similarity(set_a, set_b):
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    return len(intersection) / len(union)