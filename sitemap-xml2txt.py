# -*- coding: utf-8 -*-
# ！usr/bin/python
# ==========================
import xml.etree.ElementTree as ET

print('  😜reading sitemap.xml...')
# 读取当前目录下到sitemap.xml文件
tree = ET.ElementTree(file='sitemap.xml')
root = tree.getroot()
# 写入到sitemap.txt
print('    🤪write into sitemap.txt...')
url_no = 0;
f = open('./sitemap.txt', 'w')
for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    url_no = url_no + 1
    print('    🔍find url : ', url_no)
    f.write(loc.text + "\n")
f.close()
print('  🥳successful!!!')

# -*- coding: utf-8 -*-
# ! usr/bin/python
# ==========================
import xml.etree.ElementTree as ET
# 读取当前目录下到sitemap.xml文件
tree = ET.ElementTree(file='sitemap.xml')
root = tree.getroot()
# 写入到sitemap.txt
f = open('./sitemap.txt', 'w')
for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc');
    f.write(loc.text+"\n")
f.close()
