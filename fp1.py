import urllib2
import re

def match():
    try:
        fp =urllib2.urlopen("http://sports.sina.com.cn/n/2011-03-16/15245491564.shtml")
    except:
        print "error"
        return 0
    c = fp.read()  
    print len(c)

   # p = re.compile(r"原始正文")
   # obj = p.search(c)
   # if obj:
   #     p = re.compile(r"<p>")
   #     obj = p.search(c,obj.end())
   #     begin = obj.end()
   #     p = re.compile(r"</p>")
   #     obj = p.search(c,obj.end())
   #     end = obj.start()
   #     print c[begin:end]
    p = re.compile(r"<!-- publish_helper_end -->")
    obj = p.search(c)
    if not obj:
        return 0
    #article end
    are = obj.start()

    p = re.compile(r"<!-- publish_helper name='原始正文'")
    obj = p.search(c)
    if not obj:
        return 0
    #article begin
    arb = obj.end()

    begin = arb
    while begin < are:
        p = re.compile(r"<p>")
        obj = p.search(c,obj.end())
        begin = obj.end()
        if begin >are:
            break
        p = re.compile(r"</p>")
        obj = p.search(c,obj.end())
        end = obj.start()
        print c[begin:end]
        begin = end
    return 1
    
        
