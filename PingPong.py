from Bitfinex import Bitfinex
import json
import time
import sys

BFX = Bitfinex('API_KEY', 'API_SECRET', 'https://api.bitfinex.com/v1')

def startit():

        percent_profit = 2.5
        base_amount = 0.005
        coin = 'ZECUSD'

        time.sleep(1)
        price = BFX.get_ticker(coin)
        buysig = float(price['last_price'])
        zoneh = float(float(buysig) * (1 + float(percent_profit)/100))
        sellsig = float(buysig - (zoneh - buysig)/3)
        zonel = float(sellsig - (zoneh - buysig))
        #print str(zoneh) + "/" + str(buysig) + "/" + str(sellsig) + "/" + str(zonel)

        q1 = base_amount
        q2 = base_amount * 2

        time.sleep(1)
        myorder = BFX.sell(coin,q1,buysig,"market")
        print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
        time.sleep(2)
        market_price = float(price['last_price'])

        while (market_price < zoneh and market_price > sellsig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price > zoneh):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.buy(coin,q1,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.buy(coin,q2,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        while (market_price > zonel and market_price < buysig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price < zonel):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.sell(coin,q1,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.sell(coin,q2,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        #---------------------------------------------------------------------

        while (market_price < zoneh and market_price > sellsig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price > zoneh):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.buy(coin,q1,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.buy(coin,q2,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        while (market_price > zonel and market_price < buysig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price < zonel):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.sell(coin,q1,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.sell(coin,q2,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                time.sleep(1)

        #---------------------------------------------------------------------

        while (market_price < zoneh and market_price > sellsig):
                time.sleep(2)
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])

        if (market_price > zoneh):
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.buy(coin,q1,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                #sys.exit()
                start_again()

        else:
                price = BFX.get_ticker(coin)
                market_price = float(price['last_price'])
                time.sleep(1)
                myorder = BFX.buy(coin,q1,market_price,"market")
                print(time.strftime("%d/%m/%Y : %I:%M:%S") + "Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Direction: " + str(myorder['side']) + " / Order amount: " + str(myorder['original_amount']))
                start_again()

def start_again():
        startit()

startit()
