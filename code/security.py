# This will contain important functions

users = [
    {
        'id': 1,
        'username': 'bhanu',
        'password': '9907224577'
    }
]

username_mapping = {'bhanu': {
    'id': 1,
    'username': 'bhanu',
    'password': '9907224577'
}}

userid_mapping = {1: {
    'id': 1,
    'username': 'bhanu',
    'password': '9907224577'
}}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    pass
#     continue from here.
