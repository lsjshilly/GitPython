from redis import StrictRedis,ConnectionPool

redis = StrictRedis(host='47.106.109.80',port=6379,db=0,password='521314lsj')
redis.set('name','Bob')
print(redis.get('name'))

pool = ConnectionPool(host='47.106.109.80',port=6379,db=0,password='521314lsj')
redis = StrictRedis(connection_pool=pool)

# ConnectionPool 支持url构建
# redis://[:password]@host:port/db
# rediss://[:password]@host:port/db
# unix://[:password]@host:port/db