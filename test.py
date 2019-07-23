import xml.etree.ElementTree as ET
data = '''<rss>
           <channel>
               <item foobar="1">
               	  <title>this is my fate</title>
               	</item>		
               <item foobar="2">
          		 <title>I have to struggle</title>
               	</item>
          </channel>
       </rss>'''
tree = ET.fromstring(data)
lst = tree.findall('channel/item')
for i in lst:
	print ">>>", i.getchildren()[0].text