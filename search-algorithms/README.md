# Search Algorithms in Python

This repository contains implementations of various search algorithms in Python. Searching is a fundamental operation in computer science, used to retrieve information from data structures. This repository aims to provide a comprehensive understanding of different search algorithms, including both linear and binary search methods.

## Table of Contents

- [Overview](#overview)
- [Algorithms Implemented](#algorithms-implemented)
- [Requirements](#requirements)
- [Usage](#usage)
- [Algorithm Details](#algorithm-details)
  - [Linear Search](#linear-search)
  - [Binary Search](#binary-search)
  - [Jump Search](#jump-search)
  - [Interpolation Search](#interpolation-search)
  - [Exponential Search](#exponential-search)
  - [Fibonacci Search](#fibonacci-search)
- [Performance Comparison](#performance-comparison)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository serves as a learning tool for understanding and comparing different search algorithms. Each algorithm is implemented in a standalone Python file with comments explaining the key steps. The algorithms are tested with sample data to demonstrate their usage.

## Algorithms Implemented

1. Linear Search
2. Binary Search
3. Jump Search
4. Interpolation Search
5. Exponential Search
6. Fibonacci Search

## Requirements

- Python 3.x


## Algorithm Details

### Linear Search

Linear Search is the simplest search algorithm. It checks each element of the list sequentially until the target value is found or the list ends.

**Time Complexity**: O(n)

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Binary Search

Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the target item.

**Time Complexity**: O(log n)

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

### Jump Search

Jump Search is a search algorithm for ordered lists. It works by jumping ahead by fixed steps and then performing a linear search within a block.

**Time Complexity**: O(√n)

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1
```

### Interpolation Search

Interpolation Search is an improved variant of binary search for instances where the elements in the list are uniformly distributed. Interpolation search may go to different locations according to the value of the key being searched.

**Time Complexity**: O(log log n)

```python
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1
```

### Exponential Search

Exponential Search involves two steps: finding the range where the target may be present and then performing a binary search within that range.

**Time Complexity**: O(log n)

```python
def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    n = len(arr
