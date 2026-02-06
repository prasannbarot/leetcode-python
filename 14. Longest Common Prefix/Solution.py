class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        pre = strs[0]
        for char in strs[1:]:
            while not char.startswith(pre):
                pre = pre[:-1]
                if not pre: return ""
        return pre
