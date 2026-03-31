class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # 1. 统计频率
        count = collections.Counter(hand)
        
        # 2. 从小到大处理
        for h in sorted(count):
            if count[h] > 0:
                needed = count[h] # 这一面值的牌有多少张，就要开多少个小组
                # 3. 检查后续连续的牌够不够
                for i in range(h, h + groupSize):
                    if count[i] < needed:
                        return False
                    count[i] -= needed # 扣除消耗
        return True