import requests

# from probe import user_pb2
#
# user = user_pb2.Teacher()
#
# rsp = requests.get("http://127.0.0.1:8083/someProtoBuf")
# user.ParseFromString(rsp.content)
# print(user)


rsp = requests.post("http://127.0.0.1:8083/loginJSON", json={
    "user": "bo",
    "password": "123"
})


# rsp = requests.post("http://127.0.0.1:8083/signup", json={
#     "age": 18,
#     "name": "xiaoye",
#     "email": "xiaoasdf@qq.com",
#     "password": "asdfa",
#     "re_password": "asdfa",
# })


print(rsp.text)
