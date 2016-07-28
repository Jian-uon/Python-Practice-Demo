# -*- coding: UTF-8 -*-
import urllib2
import re

class spider:

    def __init__(self):
        self.page = 1
        self.site = 'http://www.qiushibaike.com/8hr/page/'
        self.agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.agent}
        self.ok = True

    def start(self):

        while self.ok:
            self.getPage()
            self.readStorys()
            self.page += 1
            input = raw_input("Press enter key to continue.Press Q to quit...")

    def getPage(self):
        try:
            request = urllib2.Request(self.site + str(self.page), headers=self.headers)
            self.content = urllib2.urlopen(request).read().decode('utf-8')
        except urllib2.URLError, e:
            print e.code
            print e.reason
            input = raw_input("Press enter key to exit.")
            return

    def readStorys(self):
        pattern = re.compile('<div class="author clearfix">(.*?)<h2>(.*?)</h2>(.*?)<div class="content">(.*?)</div>', re.S)
        s = re.findall(pattern, self.content)
        for item in s:
            print u'作者: ' + item[1] + '  ' + item[3]



if __name__ == '__main__':
    a = spider()
    a.start()




