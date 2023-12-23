import requests
import json

#GET -> getting the data
'''
user_input = input("enter id: ")
get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"

get_response = requests.get(get_url)

print(get_response.json())
'''

#POST -> posting the data

to_do_item = {"userId" : 3, "title" : "my to do2", "completed" : False}
post_url = "https://jsonplaceholder.typicode.com/todos"
header = {"Content_Type" : "application/json"}
#post_response = requests.post(post_url,json=to_do_item,headers=headers)
post_response = requests.post(url=post_url, data=to_do_item, headers=header)
#post_response = requests.post(post_url, data= json.dumps(to_do_item), headers=headers)
print(post_response.json())
print(post_response.status_code)
print(json.dumps(to_do_item))
print(type(json.dumps(to_do_item)))
print(type(to_do_item))