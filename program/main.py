import os, json, asyncio, logging
import time
from pprint import pprint

from modules.Account import Account
from modules.DataBase import DataBase
from modules.ASF import ASF

asf = ASF()
db = DataBase(patch='accounts.db')
db.create_table()

db.add_accounts()


async def have_game():
    pass


accounts = db.get_accounts()
async def main_program():
    while True:
        print(f'Total accounts: {len(accounts)}')
        print(f'With DST: {sum(1 for value in accounts.values() if value['dst'] is True)}')
        print('')

        print('1 - Accounts manager')

        print('')
        inpt = '1'

        match inpt:
            case '1':
                print('1 - Show all info')

                print('')
                inpt = '1'
                match inpt:
                    case '1':
                        for acc in accounts:
                            have_game = await asf.have_game(account_login=acc, game="Don't Starve Together")
                            if have_game:
                                db.set_have_game(account_login=acc, game='DST')
                            await asyncio.sleep(0)




            case '2':
                pass

            case '3':
                pass

            case _:
                break

        time.sleep(9999)


async def main():
    await asyncio.gather(main_program())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass