class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


print(Comment("john", "Hello, my friend", 3).__dict__)
print(Comment("john", "Hello, my friend").__dict__)

# Втори начин
# class Comment:
#     def __init__(self, username, content, likes=0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#
# comment = Comment("user1","I like this book")
# print(comment.username)
# print(comment.content)
# print(comment.likes)
