class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.time = 0
        self.tweets=[]
        heapq.heapify(self.tweets)
        #{'1':{followers:[]}}
        #tweets (id, userid)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        currTweet =(-self.time,userId, tweetId)
        heapq.heappush(self.tweets, currTweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        NewsFeed = []
        Temp = []

        while self.tweets and len(NewsFeed) < 10:

            # Pop the newest tweet from the heap
            tweet = heapq.heappop(self.tweets)
            Temp.append(tweet)

            # tweet = (-time, userId, tweetId)
            if tweet[1] == userId or tweet[1] in self.users[userId]:
                NewsFeed.append(tweet[2])

        # Put all tweets back into the original heap
        for tweet in Temp:
            heapq.heappush(self.tweets, tweet)

        return NewsFeed
    def follow(self, followerId: int, followeeId: int) -> None:
        #followerId followers followeeId
        self.users[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #follower unfollows followee
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)