import redis

r = redis.Redis(
    host='localhost',
    port=6379)


"""
r = redis.Redis(
    host='hostname',
    port=6379, 
    password='password')
"""

r.set('email', 'ravi@gmail.com')
value = r.get('email')
print(value)