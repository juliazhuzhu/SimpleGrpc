

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
    age = IntegerField(default=18, verbose_name="年龄")


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)


if __name__ == "__main__":
    # db.connect()
    # db.create_tables([User,Tweet])
    try:
        charlie = User(username="charlie1")
        charlie.save()
    except ValueError as e:
        print("eerrrr")
        print(e)
    #charlie = User(username="charlie")
    #charlie.save(force_insert=True)

    #henrry = User.create(username="henrry")

    #get
    # 1.return the object of object.
    # 2.throw exception if object is not found.
    # 3. only one record
    try:
        User.get(User.username == "henrry")
    except User.DoesNotExist as e:
        print(e)

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


    #update data
    charlie = User(username="charlie")
    rows = charlie.save()
    if rows == 0:
        print("not update any data!")

    print(User.update(age=20).where(User.username=="charlie").execute())

    #delete data
    # user = User.get(User.username=="henrry")
    # user.delete_instance()

    query = User.delete().where(User.username=="charlie")
    print(query)
    query.execute()

    #少量方法直接执行SQL语句, get get_by_id
