# define asset
# IN: keyboard
# OUTPUT: string

# POINT  ECHO: INITIAL CHECK(2h)
# check position: ask the API if we have open position with asset
    # IN: asset(string)
    # OUT: True(exist)/False(DNE)
# check if tradable
    # IN: asset(string)
    # OUT: True(exist)/False(DNE)



# GENERAL TREND
# load 30mins candles: demand API the 30min candles
    # IN: asset (or whatever the API needs), time range*, cnadle size*, etc.
    # OUT: 30 mins candle, (OHLC,open high close low, data for all candles )
# perform general trend analysis: detect interesting trend(up / down / no trend)
    # IN: 30 min candles data(CLose data)
    # OUT: up / down/ no trend(go back to POINT ECHO)


    # LOOP until timeout reached, e.g.30mins, then go back to 1
    # POINT DELTA
    # STEP1: load 5 mins data
        # IN: asset (or whatever the API needs), time range*, cnadle size*, etc.
        # OUT: 5 mins candle, (OHLC,open high close low, data for all candles)
        # If failed go back to POINT DELTA
    # STEP2: perform instant trend analysis
        # IN: 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
        # OUT: True(confirmed)/False(not confirmed)
        # If failed go back to POINT DELTA
    # STEP3: perform RSI analysis
        # IN: 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
        # OUT: True(confirmed)/False(not confirmed)
        # If failed go back to POINT DELTA
    # STEP 4: perform stochastic analysis
        # IN: 5 min candles data(CLose data), output of GT analysis (UP / DOWN string)
        # OUT: True(confirmed)/False(not confirmed)
        # If failed go back to POINT DELTA



# SUBMIT ORDER
# submit order: interact with API
    # IN: # of shares to operate, asset, desired price
    # OUT: True(confirmed) / False(not comfirmed), position id
    # If False; go back to POINT ECHO
# check position
    # IN: position id
    # OUT: True(confirmed) / False(not comfirmed)
    # If False; go back to POINT ECHO

# LOOP until timeout reached (ex. ~8h)
# "ENTER POSITION" MODE: OR gate conditions
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

#GET OUT
#submit order
    # IN: # of shares to operate, asset, position id
    # OUT: True(confirmed) / False(not comfirmed)
    # If False; retry until it works
#check position
    # IN: position id
    # OUT: True(still exist!) / False(not comfirmed)
    # If False; retry until it works


#wait 15mins
#back to beginning
