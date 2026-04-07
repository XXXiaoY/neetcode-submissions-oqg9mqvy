class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # 1. 将 list 转为 set，提高查询效率至 O(1)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # 2. 初始化队列：(当前单词, 当前路径长度)
        # 题目要求返回序列长度，beginWord 算第一个，所以初始长度为 1
        queue = deque([(beginWord, 1)])
        
        # 3. BFS 过程
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level
            
            # 尝试改变单词的每一个位置
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    # 生成新单词
                    next_word = current_word[:i] + char + current_word[i+1:]
                    
                    # 如果新单词在词典中，且不是自己
                    if next_word in wordSet:
                        queue.append((next_word, level + 1))
                        # 关键：访问后立即从 set 中删除，防止重复访问导致死循环
                        wordSet.remove(next_word)
        
        return 0