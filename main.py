from firebase_admin.exceptions import FirebaseError
from utils.admin import db, auth

from flask import escape

def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)

    if request_json and 'name' in request_json:
        name = request_json['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))

def sign_up(request):
    request_json = request.get_json(silent = True)
    print(request_json)
    try:
        user = auth.create_user(email = request_json["email"], password = request_json["password"])
        doc_ref = db.collection("USERS").document(user.uid)
        doc_ref.set({
            "name": request_json["name"],
            "mobile_number": request_json["mobile_number"],
            "email": request_json["email"]
        })
    except ValueError as valErr:
        print(valErr)
    except FirebaseError as fbErr:
        print(fbErr)
    return 'Signed up called'
        
    