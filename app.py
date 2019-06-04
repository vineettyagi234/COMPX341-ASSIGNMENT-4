import math 
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)



def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)




@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)



@app.route('/isPrime/<int:num>')
def isPrime(num):
    if num > 1:
      if not cache.sismember("listIsPrime", num):
       for i in range(2, math.ceil(math.sqrt(num))):
         if (num % i) == 0:
            return str(num) + " " + "is NotPrime"
       else:
            addPrime(num)
            return str(num) + " " +  "is Prime"
      else:
        return str(num) + " "  + "is Prime"
    else:
        return str(num) + " " +  "is NotPrime"


def addPrime(num):
    cache.sadd('listIsPrime', num)


@app.route('/storePrime')
def storePrime():
  numbers = cache.smembers('listIsPrime')
  number = ''
  for i in numbers:
    i.decode("utf-8")
    number += i.decode("utf-8") + "\n"
  return number
