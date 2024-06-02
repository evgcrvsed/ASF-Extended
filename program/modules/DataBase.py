import sqlite3 as sq
import time
import os, json
import random
import datetime
from pprint import pprint


class DataBase:
    def __init__(self, patch: str):
        self._patch = patch

    def create_table(self):
        self.get_cursor.execute("""CREATE TABLE IF NOT EXISTS Data (
                                        account_login TEXT NOT NULL,
                                        account_password TEXT NOT NULL,
                                        account_money TEXT DEFAULT 0,
                                        
                                        DST BOOL DEFAULT False
                                        )""")
        return 1

    def get_accounts(self) -> dict:
        accounts = self.get_cursor.execute("SELECT * FROM Data",).fetchall()
        accounts_dict = {
            account[0]: {
                'password': account[1],
                'dst': bool(account[3])
            } for account in accounts
        }

        return accounts_dict

    def set_have_game(self, account_login: str, game: str) -> bool:
        self.get_cursor.execute(f'UPDATE Data SET {game} = ? WHERE account_login = ?;',(True, account_login)).connection.commit()

    def add_accounts(self) -> None:
        files_list = os.listdir('ASF/config')
        for file in files_list:
            if not file.endswith('.json') or file in ['ASF.crash', 'ASF.json']:
                continue
            with open(f'ASF/config/{file}') as file:
                data = json.load(file)

            user_data = self.get_cursor.execute("SELECT * FROM Data WHERE account_login = ?",(data['SteamLogin'],), ).fetchone()
            if user_data is None:
                self.get_cursor.execute('INSERT INTO Data (account_login, account_password) VALUES (?, ?);',(data['SteamLogin'], data['SteamPassword'],)).connection.commit()


    @property
    def get_cursor(self):
        with sq.connect(self._patch) as con:
            return con.cursor()
