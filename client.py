#!flask/bin/pytho
import requests

a = requests.get("http://localhost:5000/todo/api/v1.0/tasks")
print(a.json())
