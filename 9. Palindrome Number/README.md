# 9. Palindrome Number

**Difficulty:** Easy  
**Topics:** Math  
**Hint:** Beware of overflow when reversing the integer.

---

## Problem

Given an integer `x`, return **true** if `x` is a palindrome, and **false** otherwise.

---

## Examples

### Example 1
**Input:**  
`x = 121`  
**Output:**  
`true`  
**Explanation:**  
`121` reads the same forward and backward.

---

### Example 2
**Input:**  
`x = -121`  
**Output:**  
`false`  
**Explanation:**  
Left to right it reads `-121`, but reversed it becomes `121-`, so it is not a palindrome.

---

### Example 3
**Input:**  
`x = 10`  
**Output:**  
`false`  
**Explanation:**  
Reversed it becomes `01`, which is not the same as `10`.

---

## Constraints

- `-2^31 <= x <= 2^31 - 1`

---

## Follow‑up

Can you solve this problem **without converting the integer to a string**?

---

