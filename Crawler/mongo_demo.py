import pymongo

# 链接数据库
client = pymongo.MongoClient()
# 选择实例
person = client.test
# 选择集合
student = person.sanguo
# 操作数据
# result = student.find()

# for r in result:
#     print(r)

# print(result.next())

# 过滤条件
# result = student.find({"country": "蜀国"})
# for r in result:
#     print(r)
# 排序
# result = student.find().sort("age", pymongo.DESCENDING)
# for r in result:
#     print(r)

# 分页
# result = student.find().limit(2).skip(6)
# for r in result:
#     print(r)

# result = student.find().count()
# print(result)

# 增加数据
# data = {"name": "黄月英", "age": 18}
# student.insert_one(data)
#
# 删除
# student.remove(data)
# 更新
data = {"name": "黄月英"}
result = student.find_one(data)
print(result)
result["country"] = "蜀国"
student.update(data, {"$set": result})