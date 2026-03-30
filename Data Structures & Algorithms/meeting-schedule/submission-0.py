"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 1. 按照对象的 start 属性进行排序
        intervals.sort(key=lambda i: i.start)
        
        # 2. 记录上一个会议的结束时间
        # 初始化为负无穷，可以完美处理任何时间起点的会议
        prev_end = float('-inf')
        
        for i in intervals:
            # 3. 如果当前开始时间 < 上一个结束时间，说明重叠
            if i.start < prev_end:
                return False
            # 4. 更新结束时间
            prev_end = i.end
            
        return True
