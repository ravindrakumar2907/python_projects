import redis

r = redis.Redis.from_url( url='rediss://:password@hostname:port/0',
    password='password',
    ssl_keyfile='path_to_keyfile',
    ssl_certfile='path_to_certfile',
    ssl_cert_reqs='required',
    ssl_ca_certs='path_to_ca_cert')


r.set('email', 'ravi@gmail.com')
value = r.get('email')
print(value)