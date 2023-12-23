import requests
import json

get_url = "https://jsonplaceholder.typicode.com/todos/15"
'''
get_response = requests.get(get_url)

print(get_response.json())
'''
#PUT -> to change existing DATA (all data)

to_do_item15 = {"userId": 2, "title": "put title", "completed": False}
'''
put_response = requests.put(get_url, json=to_do_item15)
print(put_response.json())
'''

#PATCH -> to change existing DATA (some part of data)

to_do_item_patch15 = {"title": "Patch Test"}
'''
patch_response = requests.patch(get_url,json=to_do_item_patch15)
print(patch_response.json())
'''

#DELETE

delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)