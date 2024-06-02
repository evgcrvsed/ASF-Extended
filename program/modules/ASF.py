import os
import json
import time
import shutil
import aiohttp, requests
import asyncio
from pprint import pprint


class ASF:
    def __init__(self):
        self.master = 'master'
        self.url = 'http://localhost:1242/Api/Command'
        self.headers = {
        "accept": "application/json",
        "Content-Type": "application/json"}

        self.data = {"data": {"Command": ""}}

    async def have_game(self, account_login: str = None, game: str = None):
        """Есть ли игра у этого логина"""
        self.data['Command'] = f'owns {account_login} {game}'

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.url, headers=self.headers, json=self.data) as response:
                    result = await response.json()
                    # pprint(result['Result'])
                    if '1/1' in result['Result']:
                        return True
            except Exception as ex:
                print(ex)

    def send_inventory(self, login: str, game: int, game_code: int) -> None:
        """Отправляем инвентарь мастеру"""
        self.data['Command'] = f'transfer^ {login} {game} {game_code} {self.master}'

        try:
            response = requests.post(self.url, headers=self.headers, json=self.data)
        except Exception as ex:
            pass

    @staticmethod
    def rename_bots():
        files_list = os.listdir('user_data/ASF/config')
        for file in files_list:
            try:
                if file in ['ASF.db', 'ASF.json']:
                    continue
                if '.json' in file:
                    with open(f"user_data/ASF/config/{file}") as file:
                        data = json.load(file)
                    os.rename(file.name, f'user_data/ASF/config/{data["SteamLogin"]}.json')
                    if os.path.exists(f'{file.name}'.replace('json', 'db')):
                        os.rename(f'{file.name}'.replace('json', 'db'), f'user_data/ASF/config/{data["SteamLogin"]}.db')
                    if os.path.exists(f'{file.name}'.replace('json', 'maFile')):
                        os.rename(f'{file.name}'.replace('json', 'maFile'),
                                  f'user_data/ASF/config/{data["SteamLogin"]}.maFile')
                    if os.path.exists(f'{file.name}'.replace('json', 'bin')):
                        os.rename(f'{file.name}'.replace('json', 'bin'),
                                  f'user_data/ASF/config/{data["SteamLogin"]}.bin')
                    if os.path.exists(f'{file.name}'.replace('json', 'maFile.NEW')):
                        os.rename(f'{file.name}'.replace('json', 'maFile.NEW'),
                                  f'user_data/ASF/config/{data["SteamLogin"]}.maFile.NEW')
            except Exception as ex:
                print(ex)
