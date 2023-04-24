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

Non Functional Requirements:

- Highly Available
- Reliable/durable wrt posted content and follow activity
- Feed Timeline should have low latency
- Eventual consistency is acceptable wrt to Likes/Comments Activity
- Huge Storage

Scale Constraints:

- 500M total users
- 1M DAU, posting 2 post per day 5 times timeline
- Each timeline calls 20 posts
QPS:
- Write - 2M photos/day ~ 2*[6]/8*[4] = 200/8 ~ 25/sec
- Read 10 *b 0f read = 250/sec

Stroage:

- 200 kb avg side
- 4*[11] = 400GB per Day
- 400 * 370 * 10 ~ 1480TB in 10 years
User Experience:
 - Online user will have a persistent connection to updates in timeline or activity.
 - could continuously polling but on server and client.
 - Instead, users could choose use websocks or SSE. Efficient from resources perspective
 - Offline users could be send notifications on updates 
 - All the activity messages should be fed into systems like analytics and ELK
 - Analytics can better rank the posts in a users timeline 
 - We can also show better and relevant ads to users based on their like and dislikes. Beneficial to both company, producers and consumers
 - Dashboards for campaigners
 Logging/ELK/Metrics:
 - Altering on KPIs
 - Dashboards for On calls
 
 Trade Offs:

 - How much frequent Polling
    - frequent could lead to wastage of resources
    - SSE or webstocks are better because evenets are sent only when activity happens
  - Cache Size
    - can store only too much of data 
    - Ideally should store of recent data 
    - If not, cache can become too huge
    - No precomputation for infrequent users
    - intelligent precomputation based on usage patterns during the day

Class Design:

 

Link: https://viewer.diagrams.net/index.html?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Instagram%20System%20Design#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1FuBbA4tnHFlh5eZQ5o0ytSlPhN_hWbTl%26export%3Ddownload



Schema Design:

 

Link: https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1cCRENCpGkhuADxEQpXm2VwsOWzh46dkc%26export%3Ddownload


APIS:

-	UploadMedia (UserToken , MediaContenet , MediaMetadata)
- -cloudPathUrl
    - 	CreatePost(UserToken,cloudPathUrl,Location,caption,metadata)
    
-	followUsers(UserToken,followUserId)
-	- success/failure
LikePost(UserToken,ContentId)
CommentPost(UserToken,ContentId)
getProfile(UserToken,Offset,pagesize)
getUserprofile(UserToken,UserId,Offset,pagesize)
getFeedTimeline(UserToken,pagesize)
