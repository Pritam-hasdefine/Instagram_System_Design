# Instagram_System_Design

Functional Requirements:
-	[signup] A user can signup to the system
-	[login] A user will be able to login to the system and the session will be created and used across for the other commands. Any existing session will be reinitiated with the new user logins.
-	[post] A user can post a feed item.
-	[follow] Users can follow other users.
-	[reply] A user can comment on another user's feed item.
-	[upvote/downvote] Upvote or downvote posts.
-	[shownewsfeed] Any user can read his news feed. News items are sorted based on the following (following options to sort feed by are available):
o	Followed users: posts by followed users appear first.
o	Score (= upvotes - downvotes): higher the better.
o	The number of comments: higher the better.
o	Timestamp: more recent the better.
-	Allow users to comment on a comment and upvote/downvote a comment.
-	Display time in language like 2m ago, 1 hr ago etc.

-	Input and output

-	The input should be taken in the form of commands input via the command line. The statements should consist of commands and arguments. Commands can include ‘signup’, ‘newsfeed’, ‘upvote’ etc. Arguments can vary depending on the commands
