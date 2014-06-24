import json
import urllib2
import os
import download
class Base(object):
    def __init__(self,url):
        self.url = url
    def connect(self):
        try:
            self.a = urllib2.urlopen(self.url)           
            return self.a
        except Exception,e:
            print e
            return 0

    def createDir(self,mypath):
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        
    def scrape(self):
        try:
            data=json.load(self.a)
            mylist = data['response']['results']    
            for elem in mylist:
                mypath = elem['webUrl'].split('/')[-1]
                self.createDir(mypath)                
                
                downloadLocationPath = elem['webUrl'].split('/')[-1]
                #Till what level you want the program should go and download the images
                level =  0
                #Images greater than minImageFileSize(Bytes) will be downloaded 
                minImageFileSize = 1000
                download.downloadImages(elem['webUrl'], level,downloadLocationPath,minImageFileSize)                
        except Exception,e:
            print e

class Guardian(Base):
    def __init__(self,url):
        self.url = url       
        super(Guardian,self).__init__(url)
    def extract(self):        
        con = super(Guardian,self).connect()
        if con:
            super(Guardian,self).scrape()
        else:
            print "Not able to Connect to URL "+str(self.url)
            return 0

obj = Guardian('http://content.guardianapis.com/search?q=obama&format=json')
obj.extract()
        
        
        

        
    
