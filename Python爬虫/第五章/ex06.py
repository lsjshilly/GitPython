import pymongo

client = pymongo.MongoClient(host='47.106.109.80',port=27017)
db = client.test
collection = db.students

student1 = {
    'id': "2140101086",
    'name': 'Mark',
    'age': 20,
    'gender': 'male'
}


student2 = {
    'id': "2140101087",
    'name': 'Mairy',
    'age': 20,
    'gender': 'female'
}


student3 = {
    'id': "2140101088",
    'name': 'Maliya',
    'age': 25,
    'gender': 'female'
}

# result = collection.insert_many([student3,student2])
# print(result)

# 查找用find_one find 函数 返回的时生成器对象

results = collection.find({'age': 20})
print(results)
for student in results:
    print(student)
    print(student['name'])

# $lt 小于  $gt 大于   $lte 小于等于  $gte 大于等于  $ne 不等于  $in 在范围内 $nin 不在范围内
#  $regex 指定正则匹配
#  $exists 属性是否存在
# $type 类型判断
# $mod 数字模算
# $text 文本查询
# $where 高级查询
print('大于20岁')
results2 = collection.find({'age': {'$gt': 20}})
for student2 in results2:
    print(student2)
    print(student2['name'])
print('名字以M开头')
results3 = collection.find({'name': {'$regex': '^M.*'}})
for student3 in results3:
    print(student3)
    print(student3['name'])


# 计数 count()方法
count = collection.find().count()
print(count)
count = collection.find({'age': 20}).count()
print(count)

# 排序 sort()方法
# pymongo.ASCENDING 指定升序  可以传人 pymongo.DESCENDING
results = collection.find().sort('name', pymongo.ASCENDING)
print([result4['name'] for result4 in results])

# 偏移  利用skip()忽略前几个元素
results = collection.find().sort('name', pymongo.ASCENDING).skip(3)
print([result5['name'] for result5 in results])

results = collection.find().sort('name', pymongo.ASCENDING).skip(3).limit(3)
print([result6['name'] for result6 in results])

# 更新 update_one()更新一个   updata_may() 更新多个
condition = {'age': 20}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update_one(condition, {'$set': student})
print(result.matched_count, result.modified_count)


results = collection.update_many(condition, {'$inc': {'age': 1}})
print(results.matched_count, results.modified_count)


# 删除 remove() 方法

result = collection.remove({'name': 'Mark'})
print(result)
print(collection.find_one({'name': "Mark"}))