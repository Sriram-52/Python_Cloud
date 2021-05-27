from firebase_admin.auth import CertificateFetchError, ExpiredIdTokenError, InvalidIdTokenError, RevokedIdTokenError
from flask_restful import abort
from utils.admin import auth


def close_end(req):
  token = req.headers['Authorization'].split().pop()
  try:
    decoded_token = auth.verify_id_token(token)
    print(decoded_token)
  except ValueError as val:
    print(val)
    abort(422, message="id_token is a not a string or is empty")
  except InvalidIdTokenError as invalidId:
    print(invalidId)
    abort(404, message="id_token is not a valid Firebase ID token")
  except ExpiredIdTokenError as expiredId:
    print(expiredId)
    abort(403, message="the specified ID token has expired")
  except RevokedIdTokenError as revokedId:
    print(revokedId)
    abort(403, message="You're un authorized")
  except CertificateFetchError as certErr:
    print(certErr)
    abort(500, message="Cannot fetch certificates")
