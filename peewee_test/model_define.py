

import datetime
from peewee import *
import logging

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
#db = SqliteDatabase('my_app.db')

db = MySQLDatabase('peewee', host='127.0.0.1', user='root', passwd='123456')

class BaseModel(Model):

    class Meta:
        database = db

class User(BaseModel):
    #if promary key is not set, a ID primary key automatically gen
    username = CharField(primary_key=True, max_length=20)

    class Meta:
        database = db


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)


if __name__ == "__main__":
    db.connect()
    db.create_tables([User,Tweet])

    #charlie = User(username="charlie")
    #charlie.save()

    #henrry = User.create(username="henrry")

    #get
    # 1.return the object of object.
    # 2.throw exception if object is not found.
    # 3. only one record
    try:
        #henrry = User.get(User.username=="henrry")
        henrry = User.get_by_id("henrry")
    except User.DoesNotExist as e:
        print (e)
    #print(henrry)

    #get all
    users = User.select()
    for user in User.select():
        print(user.username)

    usernames = ["charlie","henrry", "mickey"]
    users = User.select().where(User.username.in_(usernames))
    for user in users:
        print(user)
