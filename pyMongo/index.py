# 注：在使用pymongo之前 要先安装哦: pip install pymongo
import pymongo


# URL地址和要创建的数据库名。
uri = 'mongodb://localhost:27017/'

# 创建数据库需要使用 MongoClient 对象
client = pymongo.MongoClient(uri)

# print(client)


# 获取已存在的数据库 返加的是一个数组[]

# 以前的旧方法
# dblist = client.database_names()
dblist = client.list_database_names()

# print(dblist)

if "myweb" in dblist:
    print("数据库已存在！")
     # 初始化数据库
    db = client['myweb']

    # 初始化集合
    user = db["users"]

    # 获取user集合中的文档
    # info = user.find()
    print(user)

    # 更新数据，如果字段存在更新，不存在就创建
    resup = user.update_one({"username": "沐枫"},
        {"$set": { "age": 29, "phone": "18198353918"} }
    )
    print(resup)
    
else:
    # 注：这里不需要提前创建数据库和集合！！因为在向集合中插入数据时会自创建 

    # 初始化数据库
    db = client['myweb']

    # 初始化集合
    user = db["users"]

    # 向user集合插一条数据
    data = {"username": "沐枫", "password": "123456", "sex": 1, "age": 28, "email": "muguilin@foxmail.com"}
    res = user.insert_one(data)
    print(res)

    