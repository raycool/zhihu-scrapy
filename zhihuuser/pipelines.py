# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class MongoPipeline(object):

    def __init__(self):
        self.mongo_host = settings['HOST']
        self.mongo_port = settings['PORT']
        self.mongo_db = settings['DB']

        client = pymongo.MongoClient(self.mongo_host,self.mongo_port)
        self.db = client[self.mongo_db]
        self.mongo_coll = self.db[settings['COLLECTION']]


    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_host,self.mongo_port)
    #     self.db = self.client[self.mongo_db]
    #     self.mongo_coll = self.db[settings['COLLECTION']]



    def process_item(self, item, spider):
        # self.db[self.mongo_coll].update({'url_token': item['url_token']}, {'$set': dict(item)}, True)
        self.mongo_coll.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
