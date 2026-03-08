# Interview Answers

## Q1. Tuple Immutability Trap

Given:

```python
t = ([1, 2], [3, 4])


def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates


    def unique_to_each(a, b):
    result = set(a) - set(b)
    return list(result)


    unique_to_each([1, 2, 3], [3, 4, 5])