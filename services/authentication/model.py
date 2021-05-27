from utils.admin import auth


class Model():
  def create_user(self, args):
    try:
      user = auth.create_user(email=args['email'], password=args['password'])
      print(user)
    except BaseException as e:
      raise e

  def get_user(self, args):
    uid = args['uid']
    try:
      user = auth.get_user(uid=uid)
      return {
          "uid": user.uid,
          "email": user.email,
          "custom_claims": user.custom_claims
      }, 200
    except BaseException as e:
      raise e

  def delete_user(self, args):
    uid = args['uid']
    try:
      auth.delete_user(uid=uid)
    except BaseException as e:
      raise e

  def update_user(self, args):
    uid = args['uid']
    phone = args['phone']
    custom_claims = args['addInfo']
    try:
      auth.update_user(uid, phone_number=phone, custom_claims=custom_claims)
    except BaseException as e:
      raise e
