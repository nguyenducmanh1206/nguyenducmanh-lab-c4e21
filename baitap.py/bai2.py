from flask import Flask
bai2 =Flask(__name__)
item={

    "manh" : {
        "ten" : "nguyen duc manh",
        "age" : 20
    },

    "quang" : {
        "ten" : "le nhat quang",
        "age" : 20
    }

}
@bai2.route("/")
def new():
    return ("hello")
@bai2.route("/user/<username>")
def username(username):
    if username in item.keys():
        return str(item[username])
    else:
        return "khong tim duoc"
if __name__=="__main__":
    bai2.run(debug=True)






