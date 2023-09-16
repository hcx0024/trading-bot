# encoding: utf-8

# import needed library
from traderlib import *
from logger import *
import sys



# check out our trading account (blocked? total amount?)
def check_account_ok():
    try:
        #get account INFO
    except Exception as e:
        lg.error('ERROR #1: Couldn't get account info)
        lg.info(str(e))
        sys.exit()
# close current orders (double check)
def clean_open_orders():
    # get list of open orders
    lg.info('List of open orders')
    lg.info(str(open_orders))

    for order in open_orders:
        # close orders
        lg.info('Order %s closed' % str(order.id))

    lg.info('Closing orders complete')

# define asset
def get_ticker():
    # enter ticker with the keyboard
    ticker = input('Write the ticker you want to operate with: ')

    return ticker

# excute trading bot
def main():

    # initialize the logger
    initialize_logger()
    # check trading account
    check_account_ok()
    # close current account
    clean_open_orders()
    # get ticker
    ticker = input('Write the ticker you want to operate with: ')

    trader = Trader(ticker)
    # run trading bot

if __name__ == '__main__':
    main()
