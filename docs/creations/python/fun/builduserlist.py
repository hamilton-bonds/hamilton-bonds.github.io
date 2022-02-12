import pycurl
import io

def buildlist():
    info = io.StringIO()
    p = pycurl.Curl()
    p.setopt(pycurl.URL,"https://www.google.com/")
    p.setopt(pycurl.WRITEFUNCTION, info.write)
    p.perform()
    p.close()
    pinfo = info.getvalue()
    print(pinfo)

