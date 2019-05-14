# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:47:57 2019

@author: Administrator
"""


'''
mongo reader
'''


import pymongo
import re

class novel(object):
    def __init__(self):
#        self.__no=no
        pass
    def mongoset(self):
    
        client=pymongo.MongoClient('127.0.0.1:27017')
        db=client.cjdn
        collection=db.tmp
    #    bookname=[]
        chapter=[]
        bntmp=[]
        result=collection.find({},{'_id':0,'content':0})
        for i in result:
            bntmp.append(i['chapter_name'])
            chapter.append(i['chapter'])
    #    return bntmp
    #    recn=re.compile(r'节{0,1}\s*第{0,1}([十百千万零一二两三四五六七八九]*)章{0,1}')
    #    rebn=re.compile(r'节{0,1}\s*第{0,1}[十百千万零一二两三四五六七八九]*章{0,1}(.*)')
    #    for i in bntmp:
    #        c=recn.match(i).group(1)
    #        b=rebn.match(i).group(1)
    #        if not (c is None and b is None):
    #            bookname.append(b)
    #            chapter.append(c)
    #        else:
    #            bookname.append(i)
    #            chapter.append(i)
    #    return bookname,chapter,bntmp
        
        for i in range(len(chapter)):
    #        collection.update_one({'chapter_name':bntmp[i]},{'$set':{'chapter':chapter[i],'no':i,'bookname':bookname[i]}},upsert=True)
            collection.update_one({'chapter':chapter[i]},{'$set':{'no':i}},upsert=True)
            print('chapter'+chapter[i]+'update success')
    #db.tmp2.find().forEach(function(x){db.tmpo.insert(x)})
    #_id=0
    #content=0

    def mongoread(self,no):
        import pymongo
        client=pymongo.MongoClient('127.0.0.1:27017')
        db=client.cjdn
        collection=db.tmp
        rec1=r'(\xa0|\r|\n)*'
        tmpcontent=collection.find_one({'no':no})
        if tmpcontent is None:
            return
        else:
            chapter=tmpcontent['chapter']
            cpname=tmpcontent['chapter_name']
        content=tmpcontent['content']
        for i in range(len(content)):
            content[i]=re.sub(rec1,'',content[i])
        content.insert(0,chapter)
        content.insert(1,cpname)
        return content
    #    r'\xa0\r\n'
    
