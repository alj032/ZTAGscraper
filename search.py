import csv
import re


f = open('test.csv')
data = csv.reader(f)

import collections

for row in data:
 result = re.search('\/\**ZTAG(.*)ZTAG\**', (row[2]), flags=0)
 if result is not None:
  final = (row[0],result.group(0))
  y = str(final)
  x = y.replace(')','\n')
  z = x.replace("'","")
  a = z.replace("/**ZTAG-","")
  b = a.replace("-ZTAG**","")
  c = b.replace('(',"")
  d = c.replace("-",",")
  e = d.replace(" ","")
  file = open("tag.csv","a")
  file.write(str(e))
  
 else:
    bad = (row[0],row[8])
    d = str(bad)
    e = d.replace(')','\n')
    g = e.replace("('","")
    h = g.replace("'","")
    file2 = open("bad.csv","a")
    file2.write(str(h))


f.close()
file.close()
file2.close()
