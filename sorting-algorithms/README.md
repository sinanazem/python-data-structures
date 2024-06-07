# Sorting Algorithms in Python

This repository contains implementations of various sorting algorithms in Python. Sorting is a fundamental operation in computer science and is crucial for optimizing the performance of other algorithms that require sorted data.

## Table of Contents

- [Overview](#overview)
- [Algorithms Implemented](#algorithms-implemented)
- [Requirements](#requirements)
- [Usage](#usage)
- [Algorithm Details](#algorithm-details)
  - [Bubble Sort](#bubble-sort)
  - [Selection Sort](#selection-sort)
  - [Insertion Sort](#insertion-sort)
  - [Merge Sort](#merge-sort)
  - [Quick Sort](#quick-sort)
  - [Heap Sort](#heap-sort)
- [Performance Comparison](#performance-comparison)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository serves as a learning tool for understanding and comparing different sorting algorithms. Each algorithm is implemented in a standalone Python file with comments explaining the key steps.

## Algorithms Implemented

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort

## Requirements

- Python 3.x

## Usage

Clone the repository and navigate to the directory:

```sh
git clone https://github.com/your-username/sorting-algorithms.git
cd sorting-algorithms
```

You can run any of the sorting algorithms by executing the corresponding Python file. For example, to run the Bubble Sort algorithm:

```sh
python bubble_sort.py
```

Each script includes a sample list and outputs the sorted result.

## Algorithm Details

### Bubble Sort

Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

**Time Complexity**: O(n^2)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

### Selection Sort

Selection Sort divides the input list into two parts: the sorted part and the unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part.

**Time Complexity**: O(n^2)

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### Insertion Sort

Insertion Sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

**Time Complexity**: O(n^2)

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```

### Merge Sort

Merge Sort is a divide-and-conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

**Time Complexity**: O(n log n)

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

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
    return arr
```

### Quick Sort

Quick Sort is another divide-and-conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are different versions of quicksort that pick pivot in different ways.

**Time Complexity**: O(n log n)

```python
def quick_sort(arr):
    if len
