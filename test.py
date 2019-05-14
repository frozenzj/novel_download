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
    
import requests
import pytesseract as pyt
from PIL import Image
import os
class pic_test(object):
    def __init__(self):
        pass
    
    def dl_png(self):
        '''
        download png file
        '''
        for i in range(10):
            name='test'+str(i)+'.png'
            r=requests.get('http://120.76.246.143:8012/Secure/ValidateCode.aspx')
            with open(name,'wb') as f:
                f.write(r.content)
    def recognize_png(self):
        '''
        recognise the vaile code
        test
        '''
        
        os.chdir('C:/Users/Administrator/zj work files/login png')
        for i in range(10):
            img_name='test'+str(i)+'.png'
            img=Image.open(img_name)
            vcode=pyt.image_to_string(img)
            print(vcode)
            print(img)
    
if __name__=='__main__':
    print('the script is running!')
#x51=d51[['product_unit_weight','order_item_prepared_quantity']]
#y51=d51[['result_dev_weight']]
#x51train,x51test,y51train,y51test=train_test_split(data_x,data_y,test_size=0.3,random_state=1)
#l51=LinearRegression()
#l51.fit(x51train,y51train)
#l51.intercept_
#l51.coef_
#y51p=l51.predict(x51test)
#metrics.mean_squared_error(y51test,y51p)