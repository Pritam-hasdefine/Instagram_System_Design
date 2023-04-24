from datetime import datetime, timedelta

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

    def add_comment(self, text, author):
        comment = Comment(text, author)
        self.comments.append(comment)

    def upvote_comment(self, comment):
        comment.upvote()

    def downvote_comment(self, comment):
        comment.downvote()

    def score(self):
        return self.upvotes - self.downvotes

    def time_since_posted(self):
        delta = datetime.now() - self.timestamp
        if delta < timedelta(minutes=1):
            return "just now"
        elif delta < timedelta(hours=1):
            return f"{delta.seconds//60}m ago"
        elif delta < timedelta(days=1):
            return f"{delta.seconds//3600}h ago"
        else:
            return f"{delta.days}d ago"

class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.upvotes = 0
        self.downvotes = 0
        self.timestamp = datetime.now()

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes += 1

    def score(self):
        return self.upvotes - self.downvotes

    def time_since_posted(self):
        delta = datetime.now() - self.timestamp
        if delta < timedelta(minutes=1):
            return "just now"
        elif delta < timedelta(hours=1):
            return f"{delta.seconds//60}m ago"
        elif delta < timedelta(days=1):
            return f"{delta.seconds//3600}h ago"
        else:
            return f"{delta.days}d ago"

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
        comment = Comment(text, self)
        item.add_comment(comment)
        return comment

    def comment_comment(self, comment, text):
        new_comment = Comment(text, self)
        comment.add_comment(new_comment)
        return new_comment

    def upvote_item(self, item):
        item.upvote()

    def downvote_item(self, item):
        item.downvote()

    def upvote_comment(self, comment):
        comment.upvote()

