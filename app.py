from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'yarin'

api = Api(app)

@app.before_first_request
def create_tabel():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Store, '/store/<string:name>') #localhost:5000/item/<name>
api.add_resource(Item, '/item/<string:name>') #localhost:5000/item/<name>
api.add_resource(StoreList, '/stores') #localhost:5000/item/<name>
api.add_resource(ItemList, '/items') #localhost:5000/items
api.add_resource(UserRegister, '/register') #localhost:5000/register

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)