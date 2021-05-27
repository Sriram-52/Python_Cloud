from flask_restful import reqparse

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


val = 'Invalid Value'
baseEx = "Something went wrong"
key = "Invalid inputs"
