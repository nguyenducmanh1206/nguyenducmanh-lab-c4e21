
from mongoengine import Document, StringField, IntField
class Post(Document):
    title = StringField()
    author = StringField()
    content = StringField()
    password= StringField()
    likes = IntField(default=0)



