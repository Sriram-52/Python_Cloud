from flask import Flask
from flask_restful import Api
from services.authentication.controller import CreateUser

app = Flask(__name__)
api = Api(app)


api.add_resource(CreateUser, "/createUser")


if __name__ == "__main__":
    app.run(debug=True)
