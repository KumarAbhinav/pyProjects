import json
import urllib2
import os,sys
import download
#url = 'http://content.guardianapis.com/search?q=obama&format=json'
url = sys.argv[1]
try:
    data=json.load(urllib2.urlopen(url))
    mylist = data['response']['results']    
    for elem in mylist:
        mypath = elem['webUrl'].split('/')[-1]
        #If the directory does not exist create one
        if not os.path.isdir(mypath):  
            os.makedirs(mypath)
        downloadLocationPath = elem['webUrl'].split('/')[-1]
        #Till what level you want the program should go and download the images
        level =  0
        #Images greater than minImageFileSize(Bytes) will be downloaded 
        minImageFileSize = 1000
    download.downloadImages(elem['webUrl'], level,downloadLocationPath,minImageFileSize)
        
except Exception,e:
    print e
