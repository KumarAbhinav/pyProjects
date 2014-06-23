import sys
import os
import urllib2
from os.path import basename
import urlparse
from bs4 import BeautifulSoup # for HTML parsing

urlList = []

# recursively download images starting from the root URL
def downloadImages(url, level,downloadLocationPath,minImageFileSize): # the root URL is level 0    
    global urlList
    if url in urlList: # prevent using the same URL again
        return

    try:
        urlContent = urllib2.urlopen(url).read()
        urlList.append(url)
        print url
    except:
        return

    soup = BeautifulSoup(''.join(urlContent))
    # find and download all images
    imgTags = soup.findAll('img')    
    for imgTag in imgTags:        
        if imgTag.has_key('src'):
            imgUrl = imgTag['src']
            imgUrl = url[ : url.find(".com") + 4] + imgUrl if (imgUrl[ : 4] != "http") else imgUrl                    
            # download only the proper image files
            if imgUrl.lower().endswith('.jpeg') or \
                imgUrl.lower().endswith('.jpg') or \
                imgUrl.lower().endswith('.gif') or \
                imgUrl.lower().endswith('.png') or \
                imgUrl.lower().endswith('.bmp'):
                try:
                    imgData = urllib2.urlopen(imgUrl).read()                    
                    if len(imgData) >= minImageFileSize:
                        print "    " + imgUrl
                        fileName = basename(urlparse.urlsplit(imgUrl)[2])
                        output = open(os.path.join(downloadLocationPath, fileName),'wb')
                        output.write(imgData)
                        output.close()
                except Exception, e:                    
                    print str(e)

     #Recursively call function again for embedded links               
    if level > 0:
        linkTags = soup.findAll('a')
        if len(linkTags) > 0:
            for linkTag in linkTags:
                try:
                    linkUrl = linkTag['href']
                    downloadImages(linkUrl, level - 1,downloadLocationPath,minImageFileSize)                    
                except Exception, e:
                    print str(e)
                    
