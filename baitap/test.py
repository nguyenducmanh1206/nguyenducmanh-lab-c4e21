import mlab
from post import Post 

#1/
mlab.connect()
#2 create data
# p = Post(title = "C4E21", author = "manh", content = "abc", likes = 15)
# print(p.title)
# print(p.author)
# print(p.content)
# print(p.likes)
#3.wite data
# p.save()
def test_load_data():
    #2 load all documents
    all_posts =Post.objects() #lazy loading

    #3:print all documents
    for post in all_posts:

        print(post.title)
        print(post.author)
        print(post.content)
        print("..................")
def test_load_one_data(post_id):
    post = Post.objects().with_id(post_id)
    if post == None:
        print("Not Found")
    else:
        print(post.title)
        print(post.author)
        print(post.content)
# test_load_one_data("5b9cd3cb0a0400100436f13a")
def delete_one_data(post_id):
    #1.retrive document
    post = Post.objects().with_id(post_id)

    #2.delete document
    if post == None:
        print("Post not Found")
    else:
        post.delete()
delete_one_data("5b9cd3cb0a0400100436f13a")
def update_one(post_id):
    #1.retrive document
    post = Post.objects().with_id(post_id)

    #2.Update
    #slug
    post.update(set__title="New title, hihi ")
update_one("5b9cd3cb0a0400100436f13a", "Riven than kiem")