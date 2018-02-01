import urllib2
from bs4 import BeautifulSoup
source = urllib2.urlopen('http://www.rediff.com/issues/'+raw_input("Date Please: ").replace('/','')+'hl.html')
soup = BeautifulSoup(source,'html.parser')
n = soup.find('div', attrs={'id':'hdtab1'})  
p = (n.text).find('LIVE!')
print (n.text).replace('IST','IST\n')[p+5:]
