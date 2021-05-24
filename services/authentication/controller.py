from firebase_admin.exceptions import FirebaseError
from flask_restful import Resource, reqparse
from utils.admin import auth

user_post_args = reqparse.RequestParser()
user_post_args.add_argument(
    "email", type=str, help="Email of the user is req", required=True)
user_post_args.add_argument(
    "password", type=str, help="Password of the user is req", required=True)


class CreateUser(Resource):
  def post(self):
    args = user_post_args.parse_args()
    try:
      user = auth.create_user(email=args['email'], password=args['password'])
      print(user)
      return 'User created successfully', 201
    except ValueError as valErr:
      print(valErr)
      return 'Invalid value', 422
    except KeyError as keyErr:
      print(keyErr)
      return 'Invalid inputs', 422
    except FirebaseError as fbErr:
      print(fbErr)
      return str(fbErr), 500
    except BaseException as e:
      print(e)
      return 'Something went wrong', 500
