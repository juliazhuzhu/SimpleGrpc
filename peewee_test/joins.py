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
    username = TextField()

    class Meta:
        table_name = 'user2'


class Tweet(BaseModel):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref="tweets")

    class Meta:
        table_name = 'tweet2'


class Favorite(BaseModel):
    user = ForeignKeyField(User, backref="favorites")
    tweet = ForeignKeyField(Tweet, backref="favorites")


def populate_test_data():
    db.create_tables([User, Tweet, Favorite])

    data = (
        ('huey', ('meow', 'hiss', 'purr')),
        ('mickey', ('woof', 'whine')),
        ('zaizee', ()))
    for username, tweets in data:
        user = User.create(username=username)
        for tweet in tweets:
            Tweet.create(user=user, content=tweet)

    # Populate a few favorites for our users, such that:
    favorite_data = (
        ('huey', ['whine']),
        ('mickey', ['purr']),
        ('zaizee', ['meow', 'purr']))
    for username, favorites in favorite_data:
        user = User.get(User.username == username)
        for content in favorites:
            tweet = Tweet.get(Tweet.content == content)
            Favorite.create(user=user, tweet=tweet)

if __name__ == "__main__":
    # db.connect()
    # db.create_tables([User, Tweet, Favorite])

    # populate_test_data()
    # for tweet in Tweet.select():
    #     print(tweet.content, tweet.user.username)

    # #join table
    # query = Tweet.select(Tweet, User).join(User).where(User.username=="mickey")
    # print(query)
    # for q in query:
    #     print(q.user.username, q.content)
    #
    # query = Tweet.select().join(User, on=(Tweet.user==User.id))
    # print (query)
    #
    # #revert
    # tweets = User.get(User.username == "mickey").tweets
    #
    # for tweet in tweets:
    #     print(tweet.content)


 