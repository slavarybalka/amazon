import urllib 
import urllib.request


def graburlcontent(pageurl, *args): 
    opener = urllib.request.build_opener() 
    opener.addheaders = [('User-agent', 'Mozilla/5.0')] 
 
    try: 
        page = opener.open(pageurl) 
        x = page.read(*args) # number of bytes is optional
        return x.decode('UTF-8')
        

    except: 
        print("some error occured in graburlcontent function")
        pass
