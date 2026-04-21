class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF       # 32位掩码，处理Python的无限长整数
        while b & mask:
            carry = (a & b) << 1    # 进位
            a = a ^ b               # 不进位的和
            b = carry
        return a if b == 0 else a & mask
        