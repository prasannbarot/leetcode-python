# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy  
**Status:** Solved  
**Topics:** Array, Two Pointers  
**Companies:** Premium (locked)  
**Hint:** Focus on the fact that the array is sorted and use a two‑pointer approach.

---

## Problem

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should remain the same.

Let the number of unique elements in `nums` be `k`. After removing duplicates, return the value `k`.

- The first `k` elements of `nums` should contain the unique numbers in sorted order.
- The remaining elements beyond index `k - 1` can be ignored.

---

## Custom Judge

The judge will test your solution with the following code:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

---

## Examples

### Example 1

**Input:**  
`nums = [1,1,2]`

**Output:**  
`2, nums = [1,2,_]`

**Explanation:**  
Your function should return `k = 2`, with the first two elements of `nums` being `1` and `2` respectively.  
It does not matter what you leave beyond the returned `k` (hence they are underscores).

---

### Example 2

**Input:**  
`nums = [0,0,1,1,1,2,2,3,3,4]`

**Output:**  
`5, nums = [0,1,2,3,4,_,_,_,_,_]`

**Explanation:**  
Your function should return `k = 5`, with the first five elements of `nums` being `0`, `1`, `2`, `3`, and `4` respectively.  
It does not matter what you leave beyond the returned `k`.

---

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

---

## Seen in a Real Interview?

1/5  
Yes  
No

---

## Acceptance Stats

- **Accepted:** 7,610,619 / 12.2M  
- **Acceptance Rate:** 62.4%

---

## Hints

1. Since the array is sorted, duplicate elements appear next to each other.  
2. Use a two-pointer approach: one pointer for scanning, one for writing unique elements.  
3. When an element is encountered, bypass its duplicates and move to the next unique value.

