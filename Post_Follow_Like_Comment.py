from datetime import datetime

class FeedItem:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.upvotes = 0
        self.downvotes = 0
        self.comments = []
        self.timestamp = datetime.now()

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def score(self):
        return self.upvotes - self.downvotes

class User:
    def __init__(self, name):
        self.name = name
        self.following = set()

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.discard(user)

    def post_item(self, text):
        item = FeedItem(text, self)
        return item

    def comment_item(self, item, text):
        comment = FeedItem(text, self)
        item.add_comment(comment)
        return comment

    def upvote_item(self, item):
        item.upvote()

    def downvote_item(self, item):
        item.downvote()

    def news_feed(self, sort_by="followed_users"):
        items = []
        for user in self.following | {self}:
            items.extend(user.items)
        if sort_by == "followed_users":
            items = sorted(items, key=lambda item: (-item.author == self, item.timestamp), reverse=True)
        elif sort_by == "score":
            items = sorted(items, key=lambda item: (item.score(), item.timestamp), reverse=True)
        elif sort_by == "comments":
            items = sorted(items, key=lambda item: (len(item.comments), item.timestamp), reverse=True)
        elif sort_by == "timestamp":
            items = sorted(items, key=lambda item: item.timestamp, reverse=True)
        return items
