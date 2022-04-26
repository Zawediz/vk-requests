"""
Main file
"""

import time

import requests

from settings import VK_TOKEN


class Api:
    """An analogue of the official api VK"""

    def __init__(self, token):
        """Constructor"""
        self.access_token = str(token)

    def common_method(self, user_id, method, wall_method=False):
        """general view of the request"""
        user_id = str(user_id)
        method = str(method)
        if wall_method:
            temp_request = requests.get(
                "https://api.vk.com/method/" + method + "?owner_id=" +
                user_id + "&access_token=" +
                self.access_token + "&v=5.131")
        else:
            temp_request = requests.get(
                "https://api.vk.com/method/" + method + "?user_id=" +
                user_id + "&access_token=" +
                self.access_token + "&v=5.131")

        return temp_request.json()['response']

    def get_friends(self, user_id):
        """Return a list of friends"""
        method = 'friends.get'
        return self.common_method(user_id, method)

    def get_user(self, user_id):
        """The function of obtaining user information"""
        method = 'users.get'
        return self.common_method(user_id, method)

    def get_wall(self, user_id):
        """The function of getting the user's wall"""
        method = 'wall.get'
        return self.common_method(user_id, method, wall_method=True)

    def get_subscriptions(self, user_id):
        """Return subscriptions"""
        method = 'users.getSubscriptions'
        return self.common_method(user_id, method)

    def get_followers(self, user_id):
        """Return list of followers"""
        method = 'users.getFollowers'
        return self.common_method(user_id, method)

    def get_albums(self, user_id):
        """Return info about user albums"""
        method = 'photos.getAlbums'
        return self.common_method(user_id, method)


# Test class
ids = [1]
api = Api(VK_TOKEN)
# method_list = [func for func in dir(api)
#                if callable(getattr(api, func)) and not func.startswith("__")]
method_list = ['get_albums', 'get_followers', 'get_friends',
               'get_subscriptions', 'get_user', 'get_wall']
for i in ids:
    for m in method_list:
        print(m)
        print(getattr(api, m)(i))
        time.sleep(0.5)
        print()
