import urllib2
import re
class mySpider:

    def __downURL(url,filename):
       # try:
       #     fp = urllib2.urlopen(url)
       # except:
       #     print 'download exception %s'% url
       #     return 0
        op = open(filename,"wb")
        #while 1:
        #    s = fp.read()
        #    if not s:
        #        break
        #    op.write(s)

        c = match(url)
        if c == '':
            return 0
        
        op.write(c)
        
        op.close()
        return 1

    def __getURL(url):
        #pattern = re.compile("http://news.sina.com.cn/[^\>]+.shtml")
        try:
            fp = urllib2.urlopen(url)
        except:
            print 'get url exception: %s'% url
            return []
        pattern = re.compile(r"http://[A-Za-z]{1,10}?.sina.com.cn/.{1,5}?/\d{4}-\d{2}-\d{2}/\d{10,13}?.shtml")
       
        s = fp.read()
        if not s:
            return []
        urls = pattern.findall(s)

       # for z in urls:
       #     print z
            
        fp.close()
        
        return urls

    def spider(startURL,times):
        "usage: spider('www.sina.com.cn',100)"
        urls = []
        urls.append(startURL)
        i = 0
        while 1:
            if i>=times:
                break
            if len(urls)>0:
                url = urls.pop(0)
                if downURL(url,str(i)+'.txt') == 1:
                    i = i+1
                    print i,url,len(urls)
                # bloom filter is better
                if len(urls)<times:             
                    urllist = getURL(url)
                    for url in urllist:
                        if urls.count(url)==0:
                            urls.append(url)
            else:
                break
        return 1

    def __match(url):
        "将url的内容用正则表达式提取出来"
        try:
            fp =urllib2.urlopen(url)
        except:
            print "error"
            return ''
        c = fp.read()

        p = re.compile(r"<!-- publish_helper_end -->")
        obj = p.search(c)
        if not obj:
            return ''
        #article end
        are = obj.start()

        p = re.compile(r"<!-- publish_helper name='原始正文'")
        obj = p.search(c)
        if not obj:
            return ''
        #article begin
        arb = obj.start()

        if arb >= are:
            return ''

        c = c[arb:are]

        p = re.compile(r"<style type=\"text/css\">.+?</style>",re.DOTALL)
        obj = p.search(c)
        if obj:
            c = c[0:obj.start()]+c[obj.end():]

        p = re.compile(r"<script type=\"text/javascript\">.+?</script>",re.DOTALL)
        obj = p.search(c)
        if obj:
            c = c[0:obj.start()]+c[obj.end():]

            
        c = re.sub(r"<[^>]*>","",c)
        fp.close()
        return c
