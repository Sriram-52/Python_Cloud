from firebase_admin.auth import UserNotFoundError
from firebase_admin.exceptions import FirebaseError
from flask_restful import Resource, reqparse
from utils.admin import auth

user_post_args = reqparse.RequestParser()
user_post_args.add_argument(
    "email", type=str, help="Email of the user is req", required=True)
user_post_args.add_argument(
    "password", type=str, help="Password of the user is req", required=True)

user_get_args = reqparse.RequestParser()
user_get_args.add_argument(
    "uid", type=str, help="Uid is required", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument(
    "uid", type=str, help="Uid is required", required=True)
user_update_args.add_argument(
    "phone", type=str, help="Phone number is required", required=True
)
user_update_args.add_argument(
    "addInfo", type=dict, help="Custom claims of user"
)


class User(Resource):
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

  def get(self):
    args = user_get_args.parse_args()
    uid = args['uid']
    try:
      user = auth.get_user(uid=uid)
      return {
          "uid": user.uid,
          "email": user.email,
          "custom_claims": user.custom_claims
      }, 200
    except ValueError as valErr:
      print(valErr)
      return 'Invalid value', 422
    except UserNotFoundError as userErr:
      print(userErr)
      return 'No user with given uid', 400
    except FirebaseError as fbErr:
      print(fbErr)
      return 'Something went wrong', 500
    except BaseException as e:
      print(e)
      return 'Something went wrong', 500

  def delete(self):
    args = user_get_args.parse_args()
    uid = args['uid']
    try:
      auth.delete_user(uid=uid)
      return 'User deleted successfully', 203
    except ValueError as valErr:
      print(valErr)
      return 'Invalid value'
    except FirebaseError as fbErr:
      print(fbErr)
      return 'Something went wrong', 500
    except BaseException as e:
      print(e)
      return 'Something went wrong', 500

  def put(self):
    args = user_update_args.parse_args()
    uid = args['uid']
    phone = args['phone']
    custom_claims = args['addInfo']
    try:
      auth.update_user(uid, phone_number=phone, custom_claims=custom_claims)
      return 'User updated successfully', 202
    except ValueError as valErr:
      print(valErr)
      return 'Invalid value'
    except FirebaseError as fbErr:
      print(fbErr)
      return 'Something went wrong', 500
    except BaseException as e:
      print(e)
      return 'Something went wrong', 500
