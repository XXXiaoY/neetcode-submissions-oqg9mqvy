class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # 记录最长回文串的起始和结束索引
        start, end = 0, 0
        
        def expand(l: int, r: int) -> (int, int):
            """
            从中心向两边扩展，返回当前中心能达到的最远有效边界 (left, right)
            """
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # 关键：退出循环时 s[l] != s[r] 或越界
            # 所以有效回文区间是 [l + 1, r - 1]
            return l + 1, r - 1

        for i in range(len(s)):
            # 1. 奇数长度：以 s[i] 为中心
            l1, r1 = expand(i, i)
            # 2. 偶数长度：以 s[i] 和 s[i+1] 之间的空隙为中心
            l2, r2 = expand(i, i + 1)
            
            # 比较并更新全局最长坐标
            for l, r in [(l1, r1), (l2, r2)]:
                if r - l > end - start:
                    start, end = l, r
        
        # 切片截取：end 索引是包含在内的，所以切片要 +1
        return s[start : end + 1]