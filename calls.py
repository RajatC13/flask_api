import requests, json


lists = requests.get('http://localhost:5000/todos')
print(lists.json())
todo3 = requests.get('http://localhost:5000/todos/todo3')
print(todo3.json())
resp = requests.delete('http://localhost:5000/todos/todo2')
print(resp)
data = {"task" : "something new"}
data_json = json.dumps(data)
resp1 = requests.post('http://localhost:5000/todos', data={"task" : "something new"})
print(resp1)
lists = requests.get('http://localhost:5000/todos')
print(lists.json())


"""
requests.put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
todo1 = requests.get('http://localhost:5000/todo1').json()
requests.put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
todo2 = requests.get('http://localhost:5000/todo2').json()


curl http://127.0.0.1:5000/
curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
curl http://localhost:5000/todos/todo2 -X DELETE -v
curl http://localhost:5000/todos -d "task=something new" -X POST -v
curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v
"""
