# SocialMediaSystem in Python, which models a social media platform with users,
#  posts, and interactions:
class User:
    def __init__(self, username, email):
        self._username = username  # Encapsulated attribute
        self._email = email  # Encapsulated attribute
        self._posts = []  # Encapsulated attribute for user's posts
        self._followers = set()  # Encapsulated attribute for user's followers

    def create_post(self, content):
        post = Post(content, self)
        self._posts.append(post)
        print(f"{self._username} created a new post: '{content}'")

    def like_post(self, post):
        post.add_like(self)
        print(f"{self._username} liked {post._author._username}'s post")

    def follow(self, user):
        user._followers.add(self)
        print(f"{self._username} started following {user._username}")

    def display_info(self):
        print(f"Username: {self._username}")
        print(f"Email: {self._email}")
        print(f"Followers: {', '.join([follower._username for follower in self._followers])}")

    def receive_notification(self, notification):
        print(f"Notification for {self._username}: {notification}")


class Post:
    def __init__(self, content, author):
        self._content = content  # Encapsulated attribute
        self._author = author  # Encapsulated attribute
        self._likes = set()  # Encapsulated attribute for likes

    def add_like(self, user):
        self._likes.add(user)

    def display_info(self):
        print(f"Author: {self._author._username}")
        print(f"Content: {self._content}")
        print(f"Likes: {len(self._likes)}")


class SocialMediaSystem:
    def __init__(self):
        self._users = {}  # Encapsulated attribute for users

    def register_user(self, username, email):
        user = User(username, email)
        self._users[username] = user
        print(f"Registered user: {username}")

    def get_user(self, username):
        return self._users.get(username)

    def display_users(self):
        print("Registered Users:")
        for username, user in self._users.items():
            print(username)


# Creating instances of the User, Post, and SocialMediaSystem classes
social_media = SocialMediaSystem()

social_media.register_user("alice", "alice@example.com")
social_media.register_user("bob", "bob@example.com")
social_media.register_user("charlie", "charlie@example.com")

alice = social_media.get_user("alice")
bob = social_media.get_user("bob")
charlie = social_media.get_user("charlie")

alice.create_post("Hello, everyone!")
bob.create_post("Having a great day!")
charlie.create_post("New project announcement!")

alice.like_post(bob._posts[0])
charlie.like_post(bob._posts[0])

alice.follow(bob)
charlie.follow(bob)

bob.display_info()
bob._posts[0].display_info()

social_media.display_users()
