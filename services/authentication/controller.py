from firebase_admin.auth import UserNotFoundError
from firebase_admin.exceptions import FirebaseError
from flask_restful import Resource
from services.authentication.utils import user_get_args, user_post_args, user_update_args, val, key, baseEx
from services.authentication.model import Model
from end_points import close_end
from flask import request

class User(Resource):
  def post(self):
    args = user_post_args.parse_args()
    try:
      obj = Model()
      obj.create_user(args)
      return 'User created successfully', 201
    except ValueError as valErr:
      print(valErr)
      return val, 422
    except KeyError as keyErr:
      print(keyErr)
      return key, 422
    except FirebaseError as fbErr:
      print(fbErr)
      return str(fbErr), 500
    except BaseException as e:
      print(e)
      return baseEx, 500

  def get(self):
    close_end(request)
    args = user_get_args.parse_args()
    try:
      obj = Model()
      return obj.get_user(args)
    except ValueError as valErr:
      print(valErr)
      return val, 422
    except UserNotFoundError as userErr:
      print(userErr)
      return 'No user with given uid', 400
    except FirebaseError as fbErr:
      print(fbErr)
      return baseEx, 500
    except BaseException as e:
      print(e)
      return baseEx, 500

  def delete(self):
    close_end(request)
    args = user_get_args.parse_args()
    try:
      obj = Model()
      obj.delete_user(args)
      return 'User deleted successfully', 203
    except ValueError as valErr:
      print(valErr)
      return val, 422
    except FirebaseError as fbErr:
      print(fbErr)
      return baseEx, 500
    except BaseException as e:
      print(e)
      return baseEx, 500

  def put(self):
    close_end(request)
    args = user_update_args.parse_args()
    try:
      obj = Model()
      obj.update_user(args)
      return 'User updated successfully', 202
    except ValueError as valErr:
      print(valErr)
      return val, 422
    except FirebaseError as fbErr:
      print(fbErr)
      return baseEx, 500
    except BaseException as e:
      print(e)
      return baseEx, 500
