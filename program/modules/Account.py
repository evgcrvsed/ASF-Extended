import os
import json
import time


class Account:
    def __init__(self, login, password, dst: bool = False):
        self._login = login
        self._password = password

        self._dst = dst

    @property
    def get_login(self):
        return self._login

    @property
    def get_dst(self):
        return self._dst

    @property
    def get_password(self):
        return self._password

    def __str__(self):
        return f'{self._login}:{self._password}:{self._shared_secret}:{self._dst}'
