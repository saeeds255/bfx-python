from Bitfinex import Bitfinex
import json
import time
import sys

BFX = Bitfinex('API_KEY', 'API_SECRET', 'https://api.bitfinex.com/v1')

def startit():
        slprice = 2365.5
        myorder = BFX.positions()
        possymbol = str(myorder[0]['symbol'])
        posamount = float(myorder[0]['amount'])
        print("Position symbol: " + possymbol + " /Position amount: " + str(posamount) + " \n")

        price = BFX.get_ticker(possymbol)
        marketprice = float(price['last_price'])
        while (marketprice > slprice):
                time.sleep(2)
                price = BFX.get_ticker(possymbol)
                marketprice = float(price['last_price'])

        if (marketprice <= slprice):
                myorder = BFX.sell(possymbol,posamount,marketprice,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Direction: " + str(myorder['side']) + " / Price: " + str(myorder['price']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
                sys.exit()

startit()
