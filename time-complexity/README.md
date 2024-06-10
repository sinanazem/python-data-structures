# Time Complexity in Python

This repository aims to provide an understanding of time complexity, a crucial concept in computer science that helps in analyzing the efficiency of algorithms. By understanding time complexity, developers can write more efficient code and make informed decisions about which algorithms to use for specific tasks.

## Table of Contents

- [Overview](#overview)
- [Big O Notation](#big-o-notation)
- [Common Time Complexities](#common-time-complexities)
  - [Constant Time: O(1)](#constant-time-o1)
  - [Logarithmic Time: O(log n)](#logarithmic-time-olog-n)
  - [Linear Time: O(n)](#linear-time-on)
  - [Log-Linear Time: O(n log n)](#log-linear-time-on-log-n)
  - [Quadratic Time: O(n^2)](#quadratic-time-on2)
  - [Cubic Time: O(n^3)](#cubic-time-on3)
  - [Exponential Time: O(2^n)](#exponential-time-o2n)
  - [Factorial Time: O(n!)](#factorial-time-on)
- [Examples in Python](#examples-in-python)
- [How to Analyze Time Complexity](#how-to-analyze-time-complexity)
- [Contributing](#contributing)
- [License](#license)

## Overview

Time complexity is a way to express how the running time of an algorithm grows with the size of the input. It is usually expressed using Big O notation, which classifies algorithms according to their growth rates.

## Big O Notation

Big O notation is a mathematical notation used to describe the upper bound of an algorithm's running time. It provides a high-level understanding of the algorithm's performance by focusing on the most significant terms and ignoring constants and less significant terms.

## Common Time Complexities

### Constant Time: O(1)

An algorithm has constant time complexity if its running time does not depend on the size of the input.

```python
def constant_time_example(arr):
    return arr[0]
```

### Logarithmic Time: O(log n)

An algorithm has logarithmic time complexity if its running time grows logarithmically with the input size.

```python
def logarithmic_time_example(arr, target):
    low, high = 0, len(arr) - 1
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

### Linear Time: O(n)

An algorithm has linear time complexity if its running time grows linearly with the input size.

```python
def linear_time_example(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Log-Linear Time: O(n log n)

An algorithm has log-linear time complexity if its running time grows in proportion to n log n.

```python
def log_linear_time_example(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        log_linear_time_example(L)
        log_linear_time_example(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

### Quadratic Time: O(n^2)

An algorithm has quadratic time complexity if its running time grows quadratically with the input size.

```python
def quadratic_time_example(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
```

### Cubic Time: O(n^3)

An algorithm has cubic time complexity if its running time grows cubically with the input size.

```python
def cubic_time_example(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix[i][j] += matrix[i][k] * matrix[k][j]
```

