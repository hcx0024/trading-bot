# encoding: utf-8

class Trader:
    def __init__(self, ticker):
        lg.info('Trader initialized ticker %s' % ticker)

    # check if tradable
        # IN: asset(string)
        # OUT: True(exist)/False(DNE)

    # set stoploss: takes a price as input and sets the satoploss
        #IN: enter price
        #OUT: stop loss

    # set take profit: takes a price as an input and sets the take profit
        #IN: enter price
        #OUT: take profit

    # load historical stock data:
        # IN: ticker, interval, entries limit
        # OUT: array with dtock data (OHLC)

    # get open position
        # IN ticker
        #OUT: bool (T = already open / F = not open)

    # submit order: gets our order through the API(retry)
        # IN: order data, order type
        # OUT: bool (T = order went through / F = order did not)

    # cancel order: cancel our order through the API(retry)
        # IN: order id
        # OUT: bool (T = order cancelled / F = order not cancelled)

    # check position: chek whether the position is exist or not
        # IN: ticker
        # OUT: bool (T = order is there / F = order is not)

    # get general trend : detect intersting trend (UP/DOWN/NO TREND)
        # IN: 30 min candles data(CLose data)
        # OUT: up / down/ no trend(go back to POINT ECHO)

    # get instant trend: confirm the trend detected by GT analysis
        # IN: 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
        # OUT: True(confirmed)/False(not confirmed)
        # If failed go back to POINT DELTA
        
    # get rsi: perform RSI analysis
        # IN: 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
        # OUT: True(confirmed)/False(not confirmed)
        # If failed go back to POINT DELTA

    # get stochastic: perform stochastic analysis
        # IN: 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
        # OUT: True(confirmed)/False(not confirmed)

    # enter position node: check the condition in parallel
        # IF check take profit. True -> close position
            # IN: current gain (earning $)
            # OUT: True / False
        # ELIF check stop loss. True -> close position
            # IN: current gain (losing $)
            # OUT: True / False
        # ELIF check stock crossing. Pull OHLC data. If True -> close position
            # STEP 1: pull 5 mins OHLC data
                # IN: asset
                # OUT: True / False
            # STEP 2: see whether the stockastic curves are crossing
                # IN: OHLC data(5 min candles)
                # OUT: True / False

    def run():

        # LOOP until timeout reached
        # POINT  ECHO: INITIAL CHECK(2h)
        # check position: ask the API if we have open position with asset
            # IN: asset(string)
            # OUT: True(exist)/False(DNE)
        # check if tradable
            # IN: asset(string)
            # OUT: True(exist)/False(DNE)

        # Trend Analysis
        #load historical data: demand the API the 30 mins candle

        # get_general_trend()

            # LOOP until timeout reached, e.g.30mins, then go back to 1
            # POINT DELTA
            # STEP1: load historical data: demand the API the 5 mins candle
                # If failed go back to POINT DELTA

            # STEP2: get_instant trend

            # STEP3: perform rsi analysis

            # STEP 4: perform stocchastic analysis

        # SUBMIT ORDER
        # submit order (limit)
            # If False; go back to POINT ECHO
        # check position (see if position exist)
            # If False; go back to POINT ECHO

        # LOOP until timeout reached (ex. ~8h)
        # "ENTER POSITION" MODE

        #GET OUT
        #submit order (market)
            # If False; retry until it works
        #check position
            # If False; retry until it works

        #wait 15mins
        #back to beginning
