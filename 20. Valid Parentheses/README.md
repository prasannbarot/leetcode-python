# 20. Valid Parentheses

**Difficulty:** Easy  
**Status:** Solved  
**Topics:** Stack, String  
**Hint:** Use a stack to validate bracket pairs.

---

## Problem

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine whether the input string is **valid**.

A string is valid if:

- Open brackets must be closed by the **same type** of brackets.  
- Open brackets must be closed in the **correct order**.  
- Every closing bracket must have a **corresponding opening bracket**.

---

## Examples

### Example 1
**Input:**  
`s = "()"`  
**Output:**  
`true`

---

### Example 2
**Input:**  
`s = "()[]{}"`  
**Output:**  
`true`

---

### Example 3
**Input:**  
`s = "(]"`  
**Output:**  
`false`

---

### Example 4
**Input:**  
`s = "([])"`  
**Output:**  
`true`

---

### Example 5
**Input:**  
`s = "([)]"`  
**Output:**  
`false`

---

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists only of the characters `()[]{}`

---

## Additional Info

- **Seen in interviews:** Yes (1/5)  
- **Accepted:** 7,217,187 / 16.5M  
- **Acceptance Rate:** 43.7%

---

## Hints

1. Use a **stack** of characters.  
2. Push opening brackets onto the stack.  
3. When encountering a closing bracket, check whether it matches the top of the stack. If not, return `false`.

