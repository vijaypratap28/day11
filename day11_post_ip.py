import requests as r

g = r.post("http://122.181.186.42:9200/vijay", {'name':'vijay'})
print g.text
