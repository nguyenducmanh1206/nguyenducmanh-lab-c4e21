# 1 connext to database 
from pymongo import MongoClient
from bson.objectid import ObjectId
uri ="mongodb://nguyenducmanh:manh01263047222@ds029224.mlab.com:29224/nguyenducmanh"

client =MongoClient(uri)
db = client.get_default_database()
#2 select collection
posts = db["posts"]
# 3. creart document
post ={
    "title":"hôm nay trời mưa",
    "content":"t đi học code ",
}
# 4. Insert document
# posts.insert_one(post)

# print("done")
post_list=posts.find()
# for post in post_list:             #post_list~collection~list
#     print(post)
    # print(post["contend"])         #post ~ docoment~dictiona
    # print(type(post))
cond ={
    "title" :{
        "$regex":"hom nay" ,
        "$options":"i",
    }
    # "_id": ObjectId("5b855a070a040006546f0cc0")
}
post = posts.find_one(cond)
print(post)
# print(post_list[1])
