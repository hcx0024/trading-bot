# encoding: utf-8

# import needed library
from traderlib import *
from logger import *
import sys

import yfinance as yf
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST
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

def check_asset_ok(api,ticker):
# check whether the asset is ok for trading
    try:
        asset = api.get_asset(ticker)
        if asset.tradable:
            lg.info('Asset exists and tradable')
            return True
        else:
            lg.info('Asset exists but not tradable')
            sys.exit()
    except Exception as e:
            lg.error('Asset does not exists or something happens')
            lg.info(e)
            sys.exit()


# excute trading bot
def main():
    api = tradeapi.REST(gvars.API_KEY, gvars.API_SECRET_KEY, gvars.API_URL, api_version='v2')

    # initialize the logger (imported from logger.py)
    initialize_logger()
    # check trading account
    check_account_ok(api)
    # close current account
    clean_open_orders(api)

    # get ticker = assetID
    ticker = input('Write the ticker you want to operate with: ')
    # check if asset is ok for trading
    check_asset_ok(api,ticker)
    trader = Trader(ticker,api)
    # run trading bot
    tradingSuccess = trader.run(ticker)

    if not tradingSuccess:
        lg.info('Trading was not successful, locking asset')
        #wait 15mins
        time.sleep(60*15)
    else:
        lg.info('Trading was successful!')
        time.sleep(60*5)
if __name__ == '__main__':
    main()
