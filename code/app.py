from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'wanted'
api = Api(app)

# JWT creates a new endpoint named as /auth
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    # this @jwt_required will ensure that for accessing this get they have to be authenticated.
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item, 200
        # if you are expecting a list then use list()
        # item = list(filter(lambda x: x['name'] == name, items))
        # Here, I will use ''next'' so that the first item which matches will be returned.
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # silent=True will not give error it will just return none.
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': 'Block already exist. '.format(name)}, 400

        data = request.get_json(silent=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return items


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if '__main__' == __name__:
    app.run(debug=True)
