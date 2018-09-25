import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds157762.mlab.com:57762/c4e21

host = "ds157762.mlab.com"
port = 57762
db_name = "c4e21"
user_name = "nguyenducmanh"
password = "manh01263047222"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())



