class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. 初始化图和入度表
        adj = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}
        
        # 2. 建图：比较相邻单词
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # 特殊检查：如果 w1 是 w2 的前缀且更长，非法
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # 找到第一个不同的字母
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break # 后面的字母顺序无法确定
                    
        # 3. 拓扑排序 (BFS)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        res = []
        
        while queue:
            char = queue.popleft()
            res.append(char)
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 4. 如果结果长度不匹配，说明有环
        if len(res) < len(in_degree):
            return ""
            
        return "".join(res)
        