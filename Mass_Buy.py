from Bitfinex import Bitfinex
import json
import time
import sys

BFX = Bitfinex('API_KEY', 'API_SECRET', 'https://api.bitfinex.com/v1')

def startit():

  
        percent_profit = 1.5
        base_amount = 0.005
        coin = 'ZECUSD'

        price = BFX.get_ticker(coin)
        baseprice = float(price['last_price'])
        profit = percent_profit / 100
        
        p1 = baseprice
        p2 = baseprice - (profit * baseprice)
        p3 = baseprice - 2 * (profit * baseprice)
        p4 = baseprice - 3 * (profit * baseprice)
        p5 = baseprice - 4 * (profit * baseprice)
        p6 = baseprice - 5 * (profit * baseprice)
        p7 = baseprice - 6 * (profit * baseprice)
        p8 = baseprice - 7 * (profit * baseprice)
        p9 = baseprice - 8 * (profit * baseprice)
        p10 = baseprice - 9 * (profit * baseprice)
        p11 = baseprice - 10 * (profit * baseprice)
        p12 = baseprice - 11 * (profit * baseprice)
        p13 = baseprice - 12 * (profit * baseprice)
        p14 = baseprice - 13 * (profit * baseprice)
        p15 = baseprice - 14 * (profit * baseprice)
        
        time.sleep(1)
        order1 = BFX.buy(coin,base_amount,p1,"limit")
        order2 = BFX.buy(coin,base_amount,p2,"limit")
        order3 = BFX.buy(coin,base_amount,p3,"limit")
        order4 = BFX.buy(coin,base_amount,p4,"limit")
        order5 = BFX.buy(coin,base_amount,p5,"limit")
        order6 = BFX.buy(coin,base_amount,p6,"limit")
        order7 = BFX.buy(coin,base_amount,p7,"limit")
        order8 = BFX.buy(coin,base_amount,p8,"limit")
        order9 = BFX.buy(coin,base_amount,p9,"limit")
        order10 = BFX.buy(coin,base_amount,p10,"limit")
        order11 = BFX.buy(coin,base_amount,p11,"limit")
