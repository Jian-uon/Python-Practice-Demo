#This program is to download weather data from a foreign website.
import requests


class PemsDownloadSpider:
    userName = ''
    passWord = ''
    loginUrl = 'http://pems.dot.ca.gov/'
    login = 'Login'
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
    headers = {'user-agent':userAgent}
    proxies = {
        #"http": "http://172.93.33.187:443",
        "https": "http://172.93.33.187:443",
               }
    payLoad = {
        'username': userName,
        'password': passWord,
        'login': login,
    }
    Ses = requests.Session()
    Ses.keep_alive = False
    Ses.adapters.DEFAULT_RETRIES = 5
    downloadUrl = 'http://pems.dot.ca.gov/?dnode=Clearinghouse&type=fastrak_5min&district_id=all&submit=Submit'

    def signIn(self):
        re = self.Ses.post(self.loginUrl, headers=self.headers, data=self.payLoad, proxies= self.proxies)
        print re.status_code
        print re.text
        pass

    def nextStep(self):
        loadUrl = 'http://pems.dot.ca.gov/?srq=clearinghouse&district_id=all&geotag=null&yy=2013&type=fastrak_5min&returnformat=text'
        content = self.Ses.get(loadUrl).json()
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
        for month in months:
            for info in content['data'][month]:
                print 'Downloading %s...' % info['file_name']
                self.download(info['url'], info['file_name'])

    def download(self, backurl, filename):
        baseUrl = 'http://pems.dot.ca.gov'
        site = self.Ses.get(baseUrl + backurl)
        with open(filename, "wb") as code:
                code.write(site.content)

def main():
    sample = PemsDownloadSpider()
    sample.signIn()
    #sample.nextStep()
    pass

if __name__ == '__main__':
    main()