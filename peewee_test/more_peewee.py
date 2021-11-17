import datetime
from peewee import *
import logging

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
# db = SqliteDatabase('my_app.db')

db = MySQLDatabase('peewee', host='127.0.0.1', user='root', passwd='123456')


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.datetime.now, verbose_name='added time')

    class Meta:
        database = db


# class Person(BaseModel):
#     name = CharField(verbose_name='姓名', max_length=10, null=False, index=True)
#     passwd = CharField(verbose_name='password', max_length=20, null=False, default='123456')
#     email = CharField(verbose_name='邮件', max_length=50, null=True, unique=True)
#     gender = IntegerField(verbose_name='性别', null=False, default=1)
#     birthday = DateField(verbose_name='生日', null=True, default=None)
#     is_admin = BooleanField(verbose_name='是否是管理员', default=True)
#
#     first = CharField()
#     last = CharField
#
#     class Meta:
#         table_name = 'persons'
#         primary_key = CompositeKey('first', 'last')

class Person(BaseModel):
    first = CharField()
    last = CharField()

    class Meta:
        primary_key = CompositeKey('first', 'last')


class Pet(BaseModel):
    owner_first = CharField()
    owner_last = CharField()
    pet_name = CharField()

    class Meta:
        constraints = [SQL('FOREIGN KEY(owner_first, owner_last) REFERENCES person(first, last)')]


class Blog(BaseModel):
    pass


class Tag(BaseModel):
    pass


class BlogToTag(BaseModel):
    blog = ForeignKeyField(Blog)
    tag = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('blog', 'tag')


if __name__ == "__main__":
    # db.connect()
    # db.create_tables([Person, Pet, Blog, Tag, BlogToTag])

    # id = Person.insert({
    #     'first': 'xiaoye',
    #     'last': 'zhu'
    # }).execute()
    #addtime is not set
    # id = Blog.insert({}).execute()
    # print(id)
    #
    # #addtime is set by default.
    blog = Blog()
    blog.save()
    print(blog.id)

    #insert_many    一次性插入多条数据

    # blogs = [
    #     {
    #         "add_time": datetime.datetime.now()
    #     },{
    #         "add_time": datetime.datetime.now()
    #     }
    # ]
    #
    # Blog.insert_many(blogs).execute()
    #
    # #if has attribute like age, we can Person.age > 23,可以试用for loop #get对象集合
    # g = Person.select().where(Person.first == 'xiaoye').get()
    # print(g)

    person = Person.select().where((Person.first=="xiaoye")|(Person.first=="xiaoye1"))
    print (person.sql())

    person = Person.select().where((Person.first == "xiaoye") & (Person.first == "xiaoye1"))
    print(person.sql())
