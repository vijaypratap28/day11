import requests as r
import json 

g = r.get("http://122.181.186.42:9200/vijay")
json_str =  g.text
json_dict = json.loads(json_str)
print json_dict
keys = json_dict.keys()
print keys
values = json_dict.values()
print values
#print json_dict[['vijay']['settings']['index']["u'uuid'"]]
json.dumps(json_dict, indent = 5)
print json_dict

