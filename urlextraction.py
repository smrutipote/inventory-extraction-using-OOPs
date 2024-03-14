import urllib
from urllib.request import urlopen
import re

class URL():
    
    def __init__(self):
        self.url='https://docs.infor.com/bi/12.0.x/en-us/biolh_cloud/lsm1431935890525.html'

    def extract(self):
        self.data= urlopen(self.url)
        self.text=self.data.read().decode()
        #print(self.text)
    
class Modify(URL):
    
    def __init__(self):
        URL.__init__(self)
        
    def reg(self):
        self.extract()
        self.ready1=re.sub('\n+','\n',self.text)
        self.ready=re.sub('<[\w]+>','',self.ready1)
        #print(self.ready)
        self.digit=re.findall('(> 3000[0-9] <)',self.ready)
        #print(self.digit)
        #print(len(self.digit))
        self.alpha1=re.findall('[>][][A-Z ]+[][<]',self.ready)
        #print(self.alpha1)
        #print(len(self.alpha1))
        
    def ranging(self):
        self.alpha=self.alpha1[0:22]
        #print(self.alpha)
        #print(len(self.alpha))
        
obj=Modify()
obj.reg()
obj.ranging()