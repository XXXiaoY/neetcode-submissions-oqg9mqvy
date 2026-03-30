class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # userId -> [(time, tweetId), ...]
        self.followMap = defaultdict(set) # userId -> {followeeIds}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((-self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        # 关注的人包括自己
        self.followMap[userId].add(userId)
        
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweets:
                # 拿到该用户最后一条推文的索引（列表末尾）
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                # 堆存：(时间, 推文ID, 用户ID, 下一条推文的索引)
                heapq.heappush(min_heap, (time, tweetId, followeeId, index - 1))
        
        while min_heap and len(res) < 10:
            time, tweetId, f_id, idx = heapq.heappop(min_heap)
            res.append(tweetId)
            # 如果该用户还有更早的推文，继续入堆
            if idx >= 0:
                nxt_time, nxt_tweetId = self.tweets[f_id][idx]
                heapq.heappush(min_heap, (nxt_time, nxt_tweetId, f_id, idx - 1))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)