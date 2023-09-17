# encoding: utf-8

# import needed library
from traderlib import *
from logger import *
import sys
from alpaca_trade_api.rest import tradeapi
import gvars

# check out our trading account (blocked? total amount?)
def check_account_ok(api):
    try:
        account = api.get_account()
        if account.status != 'ACTIVE':
            lg.error('Accout is not ACTIVE, aborting')
            sys.exit()
    except Exception as e:
        lg.error('ERROR #1: Couldnt get account info')
        lg.info(str(e))
        sys.exit()
# close current orders (double check)
def clean_open_orders(api):

    try:
        api.cancel_all_orders()
        lg.info('All order cancelled')
    except Exception as e:
        lg.error('Could not cancel all orders')
        lg.info(str(e))
        sys.exit()


# define asset
def get_ticker():
    # enter ticker with the keyboard
    ticker = input('Write the ticker you want to operate with: ')

    return ticker

# excute trading bot
def main():
    api = tradeapi.REST(gvars.API_KEY, gvars.API_SECRET_KEY, gvars.API_URL)

    # initialize the logger (imported from logger.py)
    initialize_logger()
    # check trading account
    check_account_ok(api)
    # close current account
    clean_open_orders(api)
    # get ticker
    ticker = input('Write the ticker you want to operate with: ')

    trader = Trader(ticker)
    # run trading bot
    tradingSuccess = trader.run(ticker)

    if not tradingSuccess:
        lg.info('Trading was not successful, locking asset')
        #wait 15mins

if __name__ == '__main__':
    main()
