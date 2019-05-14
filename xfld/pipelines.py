# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class XfldPipeline(object):
    def __init__(self):
        conn=pymongo.MongoClient(host=settings['MONGODB_SERVER'],port=settings['MONGODB_PORT'])
        db=conn[settings['MONGODB_DB']]
        self.collection=db[settings['MONGODB_COLLECTION']]
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
