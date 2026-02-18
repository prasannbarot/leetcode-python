class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:           # Closing bracket
                if stack and stack[-1] == mapping[char]:
                    stack.pop()           # Match  pop
                else:
                    return False          # Mismatch  fail
            else:
                stack.append(char)        # Opening  push
        
        return not stack                  # Empty = valid
