
# https://pypi.org/project/redis/
import redis

from datetime import timedelta

r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

r.setex("name", timedelta(minutes=1), value="ravi")

data = r.get("Bahamas")
print(data)


r.set('email', 'ravi@gmail.com')
value = r.get('email')
print(value)