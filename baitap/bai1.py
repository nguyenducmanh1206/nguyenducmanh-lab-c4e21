from flask import Flask , render_template, request , redirect, url_for
import mlab
from post import Post 

mlab.connect()
bai1=Flask(__name__)
p={
    "title":"c4e21",
    "content":"moudule web",
    "author":"Quan",
    "data":"2018/12/12",
}
ps=[
    {

    }
]
@bai1.route("/posts")
def new_post():
    all_posts = Post.objects()
    return render_template("posts.html", posts=all_posts)
@bai1.route("/post/<post_id>") 
def post(post_id):    
    post = Post.objects().with_id(post_id)  
    return render_template("post.html", post=post)
@bai1.route("/delete/<post_id>")
def detele_post(post_id):
    post = Post.objects().with_id(post_id)
    if post == None:
        return " Not Found"
    else :
        post.delete()
        return "Deleted"
@bai1.route("/update/<post_id>", methods=['GET', 'POST'])       
def update(post_id):
    p = Post.objects().with_id(post_id)
    if p == None:
        return "Not found"
    else :
        if request.method == 'GET':
            return render_template('update_post.html', post = p)
        elif request.method == 'POST':
            form = request.form
            title = form['title']
            author = form['author']
            content = form['content']
            # 2.updte data
            p.update(set__title=title, set__author=author, set__content=content)
            p.reload()
            return redirect("/posts")  
    
@bai1.route("/new_posts", methods=["GET", "POST"])
def new():
    if request.method=="GET":
        return render_template("new_posts.html")
    elif request.method=="POST":
        #1.get form & extract data
        form = request.form
        title = form["title"]
        author = form["author"]
        content = form["content"]
        # print(title, author, content)
        #2.add new post
        new_post={
            "title":title,
            "author":author,
            "content":content,
            # "password":password,
        }
        ps.append(new_post)
        new_post = Post(title=title, author = author, content= content, likes=0)
        new_post.save()
        return redirect(url_for("posts")) #chuyển về đg dẫn cũ

if __name__ == "__main__":
    bai1.run(debug=True)

