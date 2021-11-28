import requests

from probe import user_pb2

user = user_pb2.Teacher()

rsp = requests.get("http://127.0.0.1:8083/someProtoBuf")
user.ParseFromString(rsp.content)
print(user)
