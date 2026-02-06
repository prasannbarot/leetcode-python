# 13. Roman to Integer

**Difficulty:** Easy  
**Status:** Solved  
**Topics:** Hash Map, String  
**Hint:** Problem is simpler when processed from **back to front** using a map.

---

## Roman Numeral Reference

Roman numerals are represented by seven symbols:

| Symbol | Value |
|--------|--------|
| I      | 1      |
| V      | 5      |
| X      | 10     |
| L      | 50     |
| C      | 100    |
| D      | 500    |
| M      | 1000   |

Examples:

- `II` = 2  
- `XII` = 12 (`X + II`)  
- `XXVII` = 27 (`XX + V + II`)

Roman numerals are usually written **largest to smallest**, left to right.

However, subtraction is used in six cases:

- `I` before `V` (5) or `X` (10) → 4, 9  
- `X` before `L` (50) or `C` (100) → 40, 90  
- `C` before `D` (500) or `M` (1000) → 400, 900  

---

## Problem

Given a Roman numeral string `s`, convert it to an integer.

---

## Examples

### Example 1
**Input:**  
`s = "III"`  
**Output:**  
`3`  
**Explanation:**  
`III = 3`

---

### Example 2
**Input:**  
`s = "LVIII"`  
**Output:**  
`58`  
**Explanation:**  
`L = 50`, `V = 5`, `III = 3`

---

### Example 3
**Input:**  
`s = "MCMXCIV"`  
**Output:**  
`1994`  
**Explanation:**  
`M = 1000`, `CM = 900`, `XC = 90`, `IV = 4`

---

## Constraints

- `1 <= s.length <= 15`
- `s` contains only: `I, V, X, L, C, D, M`
- Guaranteed valid Roman numeral in the range **[1, 3999]**

---

## Additional Info

- **Seen in interviews:** Yes (1/5)  
- **Accepted:** 5,611,376 / 8.5M  
- **Acceptance Rate:** 66.1%

