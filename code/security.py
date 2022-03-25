from werkzeug.security import safe_str_cmp
# from hmac import compare_digest
from user import User

users = [
    User(1, 'bhanu', '9907224577')
    # {
    #     'id': 1,
    #     'username': 'bhanu',
    #     'password': '9907224577'
    # }
]

username_mapping = {u.username: u for u in users}
# username_mapping = {'bhanu': {
#     'id': 1,
#     'username': 'bhanu',
#     'password': '9907224577'
# }}

userid_mapping = {u.id: u for u in users}


# userid_mapping = {1: {
#     'id': 1,
#     'username': 'bhanu',
#     'password': '9907224577'
# }}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
