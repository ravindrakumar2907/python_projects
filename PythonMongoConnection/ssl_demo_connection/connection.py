
import ConfigParser
import sys
import pymongo
#import MySQLdb
from datetime import timedelta
from datetime import datetime
import urllib

def getMongoClient():
    #client = pymongo.MongoClient(mongo_host, mongo_port)
    client = pymongo.MongoClient("mongodb://username:" + urllib.quote("password") + "@HostName:27017/customer?", 
                                 authMechanism='SCRAM-SHA-1',
                                 ssl=True, 
                                 ssl_match_hostname=False, 
                                 ssl_cert_reqs=False)
    #print client
    return client


def get_customer_details():
    db = getMongoClient().lbs
    coll = db['customer']
    customer_details = db['customer_details']
    return customer_details



data = get_customer_details().find({})
for item in data:
    print(item)

