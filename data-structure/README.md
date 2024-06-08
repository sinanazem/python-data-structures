# Python Data Structures: LinkedList, Queue, Stack, and More

This repository provides Python implementations of various fundamental data structures, including LinkedList, Queue, Stack, and more. Each data structure is implemented with explanations and examples to demonstrate their usage and functionality.

## List of Data Structures

1. [LinkedList](#linkedlist)
2. [Queue](#queue)
3. [Stack](#stack)
4. [Binary Tree](#binary-tree)
5. [Heap](#heap)
6. [Graph](#graph)
7. [Hash Table](#hash-table)
8. [Trie](#trie)

---

## LinkedList

A linked list is a linear collection of elements, where each element (node) points to the next element in the list.

### Implementation

The `LinkedList` class is implemented in Python using nodes, where each node contains data and a reference to the next node.

#### Example

```python
from linkedlist import LinkedList

# Create a new linked list
llist = LinkedList()

# Insert elements into the linked list
llist.insert(10)
llist.insert(20)
llist.insert(30)

# Print the linked list
llist.display()  # Output: 10 -> 20 -> 30
```

---

## Queue

A queue is a linear collection of elements that follows the FIFO (First In, First Out) principle.

### Implementation

The `Queue` class is implemented in Python using a list to store elements and supporting methods like `enqueue()` and `dequeue()`.

#### Example

```python
from queue import Queue

# Create a new queue
q = Queue()

# Enqueue elements into the queue
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Dequeue elements from the queue
print(q.dequeue())  # Output: 10
print(q.dequeue())  # Output: 20
```

---

## Stack

A stack is a linear collection of elements that follows the LIFO (Last In, First Out) principle.

### Implementation

The `Stack` class is implemented in Python using a list to store elements and supporting methods like `push()` and `pop()`.

#### Example

```python
from stack import Stack

# Create a new stack
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Pop elements from the stack
print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20
```

---

## Binary Tree

A binary tree is a hierarchical data structure in which each node has at most two children.

### Implementation

The `BinaryTree` class is implemented in Python using nodes, where each node contains data and references to its left and right children.

#### Example

```python
from binarytree import BinaryTree

# Create a new binary tree
tree = BinaryTree()

# Insert elements into the binary tree
tree.insert(10)
tree.insert(5)
tree.insert(15)

# Print the binary tree
print(tree)  # Output: 10
             #         / \
             #        5   15
```

---

## Heap

A heap is a specialized tree-based data structure that satisfies the heap property.

### Implementation

The `Heap` class is implemented in Python using a list to represent the heap and supporting methods like `insert()` and `extract_min()`.

#### Example

```python
from heap import Heap

# Create a new min-heap
heap = Heap()

# Insert elements into the heap
heap.insert(10)
heap.insert(20)
heap.insert(5)

# Extract the minimum element from the heap
print(heap.extract_min())  # Output: 5
```

---

## Graph

A graph is a collection of nodes (vertices) and edges that connect pairs of nodes.

### Implementation

Graphs can be implemented using various representations such as adjacency matrix or adjacency list.

#### Example (Adjacency List)

```python
from graph import Graph

# Create a new graph
graph = Graph()

# Add vertices to the graph
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)

# Add edges to the graph
graph.add_edge(1, 2)
graph.add_edge(2, 3)

# Print the graph
graph.display()  # Output: {1: [2], 2: [1, 3], 3: [2]}
```

---

## Hash Table

A hash table is a data structure that implements an associative array abstract data type, where data is stored in an array format and indexed using a hash function.

### Implementation

The `HashTable` class is implemented in Python using a dictionary to store key-value pairs.

#### Example

```python
from hashtable import HashTable

# Create a new hash table
ht = HashTable()

# Insert key-value pairs into the hash table
ht.insert('name', 'John')
ht.insert('age', 30)

# Retrieve values from the hash table
print(ht.get('name'))  # Output: John
print(ht.get('age'))   # Output: 30
```

---

## Trie

A trie is a tree-like data structure used to store a dynamic set of strings where the keys usually represent sequences.

### Implementation

The `Trie` class is implemented in Python using nodes, where each node represents a character in a string.

#### Example

```python
from trie import Trie

# Create a new trie
trie = Trie()

# Insert words into the trie
trie.insert('apple')
trie.insert('banana')
trie.insert('orange')

# Search for words in the trie
print(trie.search('apple'))   # Output: True
print(trie.search('grape'))   # Output: False
```
