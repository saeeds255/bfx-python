from Bitfinex import Bitfinex
import json
import time
import sys

BFX = Bitfinex('API_KEY', 'API_SECRET', 'https://api.bitfinex.com/v1')

def startit():

        percent_profit = 2.5
        base_amount = 0.005
        coin = 'ZECUSD'

        price = BFX.get_ticker(coin)
        buysig = float(price['last_price'])
        zoneh = float(float(buysig) * (1 + float(percent_profit)/100))
        sellsig = float(buysig - (zoneh - buysig)/3)
        zonel = float(sellsig - (zoneh - buysig))
        #print str(zoneh) + "/" + str(buysig) + "/" + str(sellsig) + "/" + str(zonel)

        q1 = base_amount

        time.sleep(1)
        myorder = BFX.buy(coin,q1,buysig,"market")
        print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
        time.sleep(2)
        market_price = float(price['last_price'])

        while (market_price < zoneh and market_price > sellsig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price > zoneh):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.sell(coin,q1,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.sell(coin,q2,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        while (market_price > zonel and market_price < buysig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price < zonel):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.buy(coin,q2exit,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.buy(coin,q3,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        #---------------------------------------------------------------------

        while (market_price < zoneh and market_price > sellsig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price > zoneh):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.sell(coin,q3exit,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.sell(coin,q4,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        while (market_price > zonel and market_price < buysig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price < zonel):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.buy(coin,q4exit,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.buy(coin,q5,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        #---------------------------------------------------------------------

        while (market_price < zoneh and market_price > sellsig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price > zoneh):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.sell(coin,q5exit,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.sell(coin,q6,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        while (market_price > zonel and market_price < buysig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price < zonel):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.buy(coin,q6exit,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.buy(coin,q7,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        #---------------------------------------------------------------------

        while (market_price < zoneh and market_price > sellsig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price > zoneh):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.sell(coin,q7exit,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                myorder = BFX.sell(coin,q8,market_price,"market")
                print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)
                myorder = BFX.buy(coin,q8exit,market_price,"market")
                start_again()
                #position = BFX.positions()
                #posamount = float(position[0]['amount'])
                #if posamount > 0:
                #        myorder = BFX.sell(coin,posamount,market_price,"market")
                    
                #elif posamount < 0:
                #        myorder = BFX.buy(coin,posamount,market_price,"market")

                #else:
                #        myorder = BFX.buy(coin,q8exit,market_price,"market")
                #start_again()

#       while (market_price > zonel and market_price < buysig):
#               time.sleep(2)
#               price = BFX.get_ticker('ETHUSD')
#               market_price = float(price['last_price'])

#       if (market_price < zonel):
#               price = BFX.get_ticker('ETHUSD')
#               market_price = float(price['last_price'])
#               myorder = BFX.buy('ETHUSD',q8exit,market_price,"market")
#               print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
                #sys.exit()
#               start_again()

#       elif (market_price > buysig):
#               price = BFX.get_ticker('ETHUSD')
#               market_price = float(price['last_price'])
#               myorder = BFX.buy('ETHUSD',q9,market_price,"market")
#               print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
#               time.sleep(2)
#               myorder = BFX.sell('ETHUSD',q9exit,market_price,"market")
#               start_again()

        #---------------------------------------------------------------------

#       while (market_price < zoneh and market_price > sellsig):
#               time.sleep(2)
#               price = BFX.get_ticker('ETCUSD')
#               market_price = float(price['last_price'])

#       orders = BFX.open_order()
        #print order[0]['id']
        #resp = BFX.cancelOrder(orders[0]['id'])
        #print resp

def start_again():
        startit()

startit()
