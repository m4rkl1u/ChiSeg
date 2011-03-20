import urllib2
import re

def downURL(url,filename):
    try:
        fp = urllib2.urlopen(url)
    except:
        print 'download exception %s'% url
        return 0
    op = open(filename,"wb")
    while 1:
        s = fp.read()
        if not s:
            break
        op.write(s)

    fp.close()
    op.close()
    return 1

def getURL(url):
    try:
        fp = urllib2.urlopen(url)
    except:
        print 'get url exception: %s'% url
        return []

    pattern = re.compile("http://sports.sina.com.cn/[^\>]+.shtml")
    while 1:
        s = fp.read()
        if not s:
            break
        urls = pattern.findall(s)
    fp.close
    return urls

def spider(startURL,times):
    urls = []
    urls.append(startURL)
    i = 0
    while 1:
        if i>times:
            break
        if len(urls)>0:
            url = urls.pop(0)
            print i,url,len(urls)
            downURL(url,str(i)+'.txt')
            i = i+1
            if len(urls)<times:
                urllist = getURL(url)
                for url in urllist:
                    if urls.count(url)==0:
                        urls.append(url)
        else:
            break
    return 1
