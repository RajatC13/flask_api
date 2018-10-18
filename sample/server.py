
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class LRUC():
    def __init__(self, maxv):
        self.limit = maxv
        self.lru = []
    def get(self, c):
        temp = self.lru[c]
        del self.lru[c]
        self.lru.insert(0, temp)
        return temp
    def put(self, elem):
        if len(self.lru) >= self.limit:
            del self.lru[len(self.lru)-1]
            self.lru.insert(0,elem)
        else:
            self.lru.insert(0,elem)

    def dele(self, index):
        a = self.lru.pop(index)
        return a


cache = LRUC(3)


parser = reqparse.RequestParser()
parser.add_argument('name')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, index):
        index = int(index)
        if index > len(cache.lru)-1:
            abort(404, message="Index doesnt exist")
        return cache.get(index)

    def delete(self, index):
        index = int(index)
        if index > len(cache.lru)-1:
            abort(404, message="Index doesnt exist")
        res = cache.dele(index)
        return '',204

    def put(self, index):
        index  = int(index)
        index = int(index)
        if index > len(cache.lru)-1:
            abort(404, message="Index doesnt exist")
        args = parser.parse_args()
        cache.lru[index] = args['name']
        return cache.lru[index], 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):

    def get(self):
        return cache.lru

    def post(self):
        args = parser.parse_args()
        cache.put(args['name'])
        return 'Created', 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<index>')


if __name__ == '__main__':
    app.run(debug=True)
