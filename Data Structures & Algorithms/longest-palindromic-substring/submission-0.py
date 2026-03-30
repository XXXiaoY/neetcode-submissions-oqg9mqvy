class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(left: int, right: int) -> int:
            # 只要左右字符相等，且不越界，就向两边推
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 返回当前回文串的长度
            return right - left - 1

        for i in range(len(s)):
            # 场景 1：以 s[i] 为中心（奇数长度）
            len1 = expandAroundCenter(i, i)
            # 场景 2：以 s[i] 和 s[i+1] 之间为中心（偶数长度）
            len2 = expandAroundCenter(i, i + 1)
            
            # 取两者中最长的
            max_len = max(len1, len2)
            
            # 如果发现更长的回文，更新起止坐标
            if max_len > (end - start):
                # 这是一个简单的几何计算：
                # start = 中心点 - 半长度
                # end = 中心点 + 半长度
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]
        