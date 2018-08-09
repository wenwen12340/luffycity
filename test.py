import redis
conn = redis.Redis(host="192.168.11.184",port=6379)

conn.set("my_name","wenwen")

val = conn.get("my_name").decode("utf-8")

print(val)