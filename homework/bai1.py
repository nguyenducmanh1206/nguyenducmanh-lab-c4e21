from flask import Flask, render_template, request
import mlab1
from post import Post 
mlab1.connect()
bai1=Flask(__name__)
ps=[
    {
        
    }

]
@bai1.route("/new", methods=["GET", "POST"])
def new():
    if request.method=="GET":
        return render_template("bai1.html")
    elif request.method=="POST":
        form = request.form
        title = form["title"]
        author = form["author"]
        content = form["content"]
        password = form["password"]
        new_post={
            "t":title,
            "e":author,
            "t":content,
            "m":password,  
        }
        ps.append(new_post)
        new_post = Post(title=title, author = author, content= content, password= password)
        new_post.save()
        return "ok"
if __name__ == "__main__":
    bai1.run(debug=True)