from urllib import urlopen
import xml.etree.ElementTree as ET

url="http://py4e-data.dr-chuck.net/comments_54824.xml"
print 'Retrieving', url
uh = urlopen(url)
data = uh.read()
print 'Retrieved', len(data), 'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total=0
for count in counts:
    total+=int(count.text)
print total
