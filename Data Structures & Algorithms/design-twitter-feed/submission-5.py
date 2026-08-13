class Twitter:

    def __init__(self):
        # userId -> set of users they follow
        self.users = defaultdict(set)

        # userId -> list of (time, tweetId)
        self.tweets = defaultdict(list)

        # Global counter to determine which tweet is newer
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        # Store this user's tweets in chronological order
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []

        # User needs to see their own tweets + people they follow
        users = self.users[userId] | {userId}

        # Put the newest tweet from each relevant user into the heap
        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                # Negative time because heapq is a min-heap
                heapq.heappush(
                    heap,
                    (-time, user, index, tweetId)
                )

        # Get the 10 newest tweets
        while heap and len(feed) < 10:

            _, user, index, tweetId = heapq.heappop(heap)

            feed.append(tweetId)

            # Move to this user's next newest tweet
            index -= 1

            if index >= 0:
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, user, index, tweetId)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)