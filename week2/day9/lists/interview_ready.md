# Interview Ready Answers

## Q1. Difference Between Shallow Copy and Deep Copy

### Shallow Copy
A shallow copy creates a new outer list, but nested inner lists still point to the same memory locations as the original list.

Example:

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 100

print("Original:", original)
print("Shallow:", shallow)
