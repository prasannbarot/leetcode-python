# 21. Merge Two Sorted Lists

**Difficulty:** Easy  
**Status:** Solved  
**Topics:** Linked List, Two Pointers  
**Companies:** Premium (locked)

---

## Problem

You are given the heads of two **sorted** linked lists `list1` and `list2`.

Merge the two lists into **one sorted linked list**.  
The merged list should be created by **splicing together the nodes** of the first two lists.

Return the **head** of the merged linked list.

---

## Examples
![merge_ex1](https://github.com/user-attachments/assets/af376e7e-912f-4b6c-9cf1-f369219e3ab7)

### Example 1
**Input:**  
`list1 = [1,2,4]`, `list2 = [1,3,4]`  
**Output:**  
`[1,1,2,3,4,4]`

---

### Example 2
**Input:**  
`list1 = []`, `list2 = []`  
**Output:**  
`[]`

---

### Example 3
**Input:**  
`list1 = []`, `list2 = [0]`  
**Output:**  
`[0]`

---

## Constraints

- Number of nodes in both lists: **0 to 50**
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non‑decreasing** order

