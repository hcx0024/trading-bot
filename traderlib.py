# encoding: utf-8
import sys
import tulipy as ti
import pandas as pd
from datetime import datetime
from math import ceil


class Trader:
    def __init__(self,ticker):
        lg.info('Trader initialized ticker %s' % ticker)
        self.ticker = ticker

    def is_tradable(self,ticker):
    # check if tradable
        # IN: ticker(string)
        # OUT: True(exist)/False(DNE)
        try:
            # ticker = get ticker frompa alpaca wrpper
            if not ticker.tradable:
                lg.info('The ticker %s is not tradable' % ticker)
                return False
            else:
                lg.info('The ticker %s is tradable' % ticker)
                return True
        except:
            lg.info('The ticker %s is not answering well' % ticker)
            return False


    def set_stoploss(self,entryPrice,trend):
    # set stoploss: takes entry price as input and sets the satoploss
        #IN: enter price
        #OUT: stop loss


        try:
            if trend == 'long':
                stopLoss = entryPrice - (entryPrice * gvars.stopLossMargin)
                return stopLoss
            elif trend == 'short':
                stopLoss = entryPrice + (entryPrice * gvars.stopLossMargin)
                return stopLoss
            else:
                raise ValueError

        except Exception as e:
            lg.error('The trendvalue is not understood %s' % str(trend))
            sys.exit()


    def set_takeprofit(self,entryPrice,trend):
    # set take profit: takes a price as an input and sets the take profit
        #IN: enter price
        #OUT: take profit

        try:
            if trend == 'long':
                takeProfit = entryPrice + (entryPrice * gvars.takeProfitMargin)
                lg.info('Take profit set for long at %.2f' % takeProfit)
                return takeProfit
            elif trend == 'short':
                takeProfit = entryPrice - (entryPrice * gvars.takeProfitMargin)
                lg.info('Take profit set for short at %.2f' % takeProfit)
                return takeProfit
            else:
                raise ValueError

        except Exception as e:
            lg.error('The trendvalue is not understood %s' % str(trend))
            sys.exit()

    # load historical stock data:
        # IN: ticker, interval, entries limit
        # OUT: array with dtock data (OHLC)

    def get_open_position(self,tickerId):
    # get open position
        # IN ticker
        #OUT: bool (T = already open / F = not open)

        # positions = # ticker = get ticker frompa alpaca wrpper
        for position in positions:
            if position.symbol == tickerId:
                return True
            else:
                return False
    # submit order: gets our order through the API(retry)
        # IN: order data, order type
        # OUT: bool (T = order went through / F = order did not)

    # cancel order: cancel our order through the API(retry)
        # IN: order id
        # OUT: bool (T = order cancelled / F = order not cancelled)
    def check_position(self,ticker,doNotFind=False):
    # check position: chek whether the position is exist or not
        # IN: ticker, doNotFind(get out earlier in getting out process)
        # OUT: bool (T = order is there / F = order is not)
        attempt = 1

        while attempt < gvars.maxAttemptsCP:
            try:
                # position = ask the alpaca wrapper for a positions
                currentPrice = position.current_price
                lg.info('The position was checked. Current price is %.2f' % currentPrice)
                return True
            except:
                if doNotFind:# when get out of market pass a T in
                    lg.info('Position not found, this is good!')
                    return False

                lg.info('Position not found, waiting for it')
                time.sleep(gavrs.sleepTimesCP) # wait for 5 sec and retry
                attempt += 1

        lg.info('Position not found for %s, not waiting any more' % ticker)
        return False


    def get_shares_amount(self,tickerPrice):
        #works out the number of shares I want to buy/Sell
            # IN: ticker entryPrice
            # OUT: number of shares

            lg.info('Getting shares amount')

            try:
                # define max to spend
                

                # get the total equity available
                # totalEquity = ask Alpaca API for available equity

                #calculate number of shares
                sharesQuantity = int(gvars.maxSpentEquity / tickerPrice)

                lg.info('Total share to operate with: %d' % sharesQuantity)

                return sharesQuantity
            except Exception as e:
                lg.error('Something happen at get share amount')
                lg.error(e)
                sys.exit()



    def get_current_price(self,ticker):
        # get the curretn price of an ticker with a position open
        attempt = 0


        while attempt < gvars.maxAttemptsGCP:
            try:
                # position = ask the alpaca wrapper for a positions
                currentPrice = position.current_price
                lg.info('The position was checked. Current price is %.2f' % currentPrice)
                return currentPrice
            except:
                lg.info('Position not found, cannot check price, waiting for it')
                time.sleep(gavrs.sleepTimesGCP) # wait for 5 sec and retry
                attempt += 1

        lg.error('Position not found for %s, not waiting any more' % ticker)
        return False


    def get_general_trend(self,ticker):
    # get general trend : detect intersting trend (UP/DOWN/NO TREND)
        # IN: ticker
        # OUT: up / down/ no trend(go back to POINT ECHO)
        lg.info('GENERAL TREND ANALYSIS entered')

        attempt = 1
        maxAttempt = 10 # EDIBLE: total time = maxAttempt * 10 mins (as implemented)

        try:
            while True:

                # data = ask alpaca wrapper for 30 mins candle

                #calculate emas
                ema9 = ti.ema(data,9)
                ema26 = ti.ema(data,26)
                ema50 =ti.ema(data,50)

                lg.info('%s general trend EMAs: [%.2f.%.2f,%.2f]' % (ticker,ema9,ema26,ema50))

                #check EMA relative position
                    #if (ema50 > ema26) and (ema26 > ema9):
                        lg.info('Trend detected for %s: long' % ticker)
                        return 'long'
                    #elif (ema50 > ema26)  and (ema26 < ema9):
                        lg.info('Trend detected for %s: short' % ticker)
                        return 'short'
                    #elif attempt <= maxAttempt
                        lg.info('Trend not clear for %s, waiting...' % ticker)
                        time.sleep(60)
                    #else
                        lg.info('Trend NOT detected and timeout reachedfor %s' % ticker)
                        return False
        except Exception as e:
            lg.Error('Something went wrong at get general trend')
            lg.error(e)
            sys.exit()


    def get_instant_trend(self,ticker,trend):
    # get instant trend: confirm the trend detected by GT analysis
        # IN: 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
        # OUT: True(confirmed)/False(not confirmed)
        # If failed go back to POINT DELTA
        lg.info("INSTANT TREND ANALYSIS entered")

        attempt = 1
        maxAttempt = 10 # EDIBLE: total time = maxAttempt * 10 secs (as implemented)

        try:
            while True:
                #data = ask alpaca for 5 mins candles

                #calculate emas
                ema9 = ti.ema(data,9)
                ema26 = ti.ema(data,26)
                ema50 =ti.ema(data,50)

                lg.info('%s instant trend EMAs: [%.2f.%.2f,%.2f]' % (ticker,ema9,ema26,ema50))

                if (trend == 'long') and (ema9 > ema26) and (ema26 > ema50):
                    lg.info('Long trend confirmed for %s' % ticker)
                    return True
                elif (trend == 'short') and (ema9 < ema26) and (ema26 < ema50):
                    lg.info('Short trend confirmed for %s' % ticker)
                    return True
                elif sttempt <= maxAttempt:
                    lg.info('Trend not clear for %s, waiting...' % ticker)
                    time.sleep(30)
                else:
                    lg.info('Trend NOT detected and timeout reached for %s' % ticker)
                    return False
        except Exception as e:
            lg.Error('Something went wrong at get instant trend')
            lg.error(e)
            sys.exit()


    def get_rsi(self,ticker,trend):
        # get rsi: perform RSI analysis
            # IN: 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
            # OUT: True(confirmed)/False(not confirmed)
            # If failed go back to POINT DELTA

        lg.info("RSI TREND ANALYSIS entered")

        attempt = 1
        maxAttempt = 10 # EDIBLE: total time = maxAttempt * 10 secs (as implemented)

        try:
            while True:
                #data = ask alpaca for 5 mins candles

                #calculate RSI
                rsi = ti.rsi(data, 14) # 14 is EDIBLE, now uses 14 samples

                lg.info('%s rsi = [%.2f]' % (ticker,rsi))

                if (trend == 'long') and (rsi > 50) and (rsi < 80):
                    lg.info('Long trend confirmed for %s' % ticker)
                    return True
                elif (trend == 'short') and (rsi < 50) and (rsi > 20):
                    lg.info('Short trend confirmed for %s' % ticker)
                    return True
                elif sttempt <= maxAttempt:
                    lg.info('Trend not clear for %s, waiting...' % ticker)
                    time.sleep(20) # 20 sec * 10
                else:
                    lg.info('Trend NOT detected and timeout reached for %s' % ticker)
                    return False

        except Exception as e:
            lg.Error('Something went wrong at rsi analysis')
            lg.error(e)
            sys.exit()


    def get_stochastic(self,ticker,trend):
    # get stochastic: perform stochastic analysis
        # IN: ticker, 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
        # OUT: True(confirmed)/False(not confirmed)
        lg.info("STOCHASTIC ANALYSIS entered")

        attempt = 1
        maxAttempt = 10 # EDIBLE: total time = maxAttempt * 10 secs (as implemented)

        try:
            while True:
                #data = ask alpaca for 5 mins candles

                #calculate STOCHASTIC
                #highest of candle, lowesest of candle, close value of candle, 5,3,3 is EDIBLE
                stoch_k, stoch_d = ti.stoch(high, low, close, 5, 3, 3)

                lg.info('%s stochastic = [%.2f, %.2f]' % (ticker,stoch_k,stoch_d))

                if (trend == 'long') and (stoch_k > stoch_d) and (stoch_k < 80) and (stoch_d < 80):
                    lg.info('Long trend confirmed for %s' % ticker)
                    return True
                elif (trend == 'short') and (stoch_k < stoch_d) and (stoch_k > 20) and (stoch_d > 20):
                    lg.info('Short trend confirmed for %s' % ticker)
                    return True
                elif sttempt <= maxAttempt:
                    lg.info('Trend not clear for %s, waiting...' % ticker)
                    time.sleep(10) # sec * #of times
                else:
                    lg.info('Trend NOT detected and timeout reached for %s' % ticker)
                    return False

        except Exception as e:
            lg.Error('Something went wrong at stochastic analysis')
            lg.error(e)
            sys.exit()


    def check_stochastic_crossing(self,ticker,trend):
        # check whether the stochastic curves have crossed or # not
        # depending on the trend

        #get stochastic values
        #data = ask alpaca for 5 mins candles

        #calculate STOCHASTIC
        #highest of candle, lowesest of candle, close value of candle, 5,3,3 is EDIBLE
        stoch_k, stoch_d = ti.stoch(high, low, close, 5, 3, 3)

        lg.info('%s stochastic = [%.2f, %.2f]' % (ticker,stoch_k,stoch_d))
        try:
            if (trend == 'long') and (stoch_k <= stoch_d):
                lg.info('Stochastic curves crossed: long, k=%.2, d=%.2f' % (stoch_k,stoch_d))
                return True
            elif (trend == 'short') and (stoch_k >= stoch_d):
                lg.info('Stochastic curves crossed: short, k=%.2, d=%.2f' % (stoch_k,stoch_d))
                return True
            else:
                lg.info('Stochastic curves never crossed')
                return False
        except Exception as e:
            lg.error('Something went wrong at check stochastic crossing')
            lg.error(e)
            return True #return true to get out immediately


    def enter_position_mode(self,ticker,trend):
    # IF check take profit. True -> close position
        # IN: current gain (earning $)
        # OUT: True / False
    # ELIF check stop loss. True -> close position
        # IN: current gain (losing $)
        # OUT: True / False
    # ELIF check stock crossing. Pull OHLC data. If True -> close position
        # STEP 1: pull 5 mins OHLC data
            # IN: ticker
            # OUT: True / False
        # STEP 2: see whether the stockastic curves are crossing
            # IN: OHLC data(5 min candles)
            # OUT: True / False
    # enter position node: check the condition in parallel

        # entryPrice = ask Alpaca API for the entry price

        # set take profit
        takeProfit = set_takeprofit(entryPrice,trend)

        #set the stop stop loss
        stopLoss = set_stoploss(entryPrice,trend)
        attempt = 1
        maxAttempt = 1260 # EDIBLE: total time = maxAttempt *  secs (as implemented) 7h fro now
        try:
            while True:
                currentPrice = get_current_price(ticker)

                # LONG ver
                if (trend == 'long') and (currentPrice >= takeProfit):
                    lg.info('Take profit met at %.2. Current price is %.2, getting out...' %(takeProfit, currentPrice))
                    return True

                # SHORT ver
                elif (trend == 'short') and (currentPrice <= takeProfit):
                    lg.info('Take profit met at %.2. Current price is %.2, getting out...' %(takeProfit, currentPrice))
                    return True

                # LONG ver
                elif (trend == 'long') and (currentPrice <= stopLoss):
                    lg.info('Stop loss met at %.2. Current price is %.2, getting out...' %(stopLoss, currentPrice))
                    return False

                # SHORT ver
                elif (trend == 'short') and (currentPrice <= stopLoss):
                    lg.info('Stop loss met at %.2. Current price is %.2, getting out...' %(stopLoss, currentPrice))
                    return False

                elif check_stochastic_crossing(ticker,trend):
                    lg.info('Stochastic curves crossed. Current price is %.2, getting out...' %currentPrice)
                    return True
                elif sttempt <= maxAttempt:
                    lg.info('Waiting inside position')
                    lg.info('%.2 <-- %.2f --> %.2f' % (stopLoss,currentPrice,takeProfit))
                    time.sleep(20)
                else:
                    lg.info('Timeout reached for enter position, too late')
                    return False
        except Exception as e:
            lg.error('Something went wrong at enter position function')
            lg.error(e)
            return True #return true to get out immediately




    def run(self):

        # LOOP until timeout reached (ex. 2h)


        while True:# POINT  ECHO: INITIAL CHECK
            # ask the API if we have open position with ticker
            if check_position(self.ticker,doNotFind=True):
                lg.info('There is already an open position with that ticker! Aborting...')
                return False #aborting excution
            # POINT DELTA
            while True:
                # get_general_trend()
                trend = get_general_trend(self.ticker)
                if not trend:
                    lg.info('No general trend found for %s! Going out...' % self.ticker)
                    return False


                # get_instant trend
                if not get_instant_trend(self.ticker,trend):
                    lg.info('No instant trend is confirm, Going back.'')
                    continue# If failed go back to POINT DELTA

                # perform rsi analysis
                if not get_rsi(self.ticker,trend):
                    lg.info('No rsi is confirm, Going back.'')
                    continue# If failed go back to POINT DELTA

                # perform stocchastic analysis
                if not get_stochastic(self.ticker,trend):
                    lg.info('No stochastic is confirm, Going back.'')
                    continue# If failed go back to POINT DELTA
                lg.info('All filtering passed, carrying on with the order')
                break

            # get current price
            self.currentPrice = get_current_price(self.ticker)

            # decide the total amount to invest
            sharesQuantity = get_shares_amount(self.ticker,self.currentPrice)

            # submit order (limit)
                # If False; go back to POINT ECHO

            # check position (see if position exist indicating sucess buy)
            if not check_position(self.ticker):
                # cancel pending order
                continue # If False; go back to POINT ECHO

            # "ENTER POSITION" MODE
            sucessfulOperation = enter_position_mode(self.ticker,trend)

            #GET OUT
            #LOOP until successful
            while True:
                #submit order (market)
                    # If False; retry until it works
                #check position
                if not check_position(self.ticker,doNotFind=True):
                    break
                time.sleep(10)# wait for 10 secs


            return sucessfulOperation
            #end of excution
