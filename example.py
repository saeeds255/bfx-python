from Bitfinex import Bitfinex
import json
import time
import sys 

BFX = Bitfinex('API_KEY', 'API_SECRET', 'https://api.bitfinex.com/v1')

percent_profit = 5
base_amount = 0.3

price = BFX.get_ticker('ETCUSD')
buysig = float(price['last_price'])
zoneh = float(buysig) * (1 + float(percent_profit)/100)
sellsig = float(buysig - (zoneh - buysig)/3)
zonel = sellsig - (zoneh - buysig)
q1 = base_amount
q2 = q1 + (base_amount * 1.4)
q2exit = q2 - q1
q3 = q2 + (base_amount * 1.4 * 1.4)
q3exit = q3 - q2
q4 = q3 + (base_amount * 1.4 * 1.4 * 1.4)
q4exit = q4 - q3
q5 = q4 + (base_amount * 1.4 * 1.4 * 1.4 * 1.4)
q5exit = q5 - q4
q6 = q5 + (base_amount * 1.4 * 1.4 * 1.4 * 1.4 * 1.4)
q6exit = q6 - q5
q7 = q6 + (base_amount * 1.4 * 1.4 * 1.4 * 1.4 * 1.4 * 1.4)
q7exit = q7 - q6
q8 = q7 + (base_amount * 1.4 * 1.4 * 1.4 * 1.4 * 1.4 * 1.4 * 1.4)
q8exit = q8 - q7
q9 = q8 + (base_amount * 1.4 * 1.4 * 1.4 * 1.4 * 1.4 * 1.4 * 1.4 * 1.4)
q9exit = q9 - q8

myorder = BFX.buy('ETCUSD',q1,buysig,"market")
print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
time.sleep(1)
market_price = float(price['last_price'])

while (market_price < zoneh and market_price > sellsig):
  time.sleep(1)
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])

if (market_price > zoneh):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.sell('ETCUSD',q1,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  sys.exit()
  
elif (market_price < sellsig):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.sell('ETCUSD',q2,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  time.sleep(1)
  
while (market_price > zonel and market_price < buysig):
  time.sleep(1)
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  
if (market_price < zonel):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.buy('ETCUSD',q2exit,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  sys.exit()
  
elif (market_price > buysig):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.buy('ETCUSD',q3,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  time.sleep(1)
  
  #---------------------------------------------------------------------
  
while (market_price < zoneh and market_price > sellsig):
  time.sleep(1)
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])

if (market_price > zoneh):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.sell('ETCUSD',q3exit,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  sys.exit()
  
elif (market_price < sellsig):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.sell('ETCUSD',q4,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  time.sleep(1)
  
while (market_price > zonel and market_price < buysig):
  time.sleep(1)
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  
if (market_price < zonel):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.buy('ETCUSD',q4exit,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  sys.exit()
  
elif (market_price > buysig):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.buy('ETCUSD',q5,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  time.sleep(1)
 
  #---------------------------------------------------------------------
  
while (market_price < zoneh and market_price > sellsig):
  time.sleep(1)
  market_price = float(price['last_price'])

if (market_price > zoneh):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.sell('ETCUSD',q5exit,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  sys.exit()
  
elif (market_price < sellsig):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.sell('ETCUSD',q6,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  time.sleep(1)
  
while (market_price > zonel and market_price < buysig):
  time.sleep(1)
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  
if (market_price < zonel):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.buy('ETCUSD',q6exit,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " /")
  sys.exit()
  
elif (market_price > buysig):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.buy('ETCUSD',q7,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  time.sleep(1)
  
  #---------------------------------------------------------------------
  
while (market_price < zoneh and market_price > sellsig):
  time.sleep(1)
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])

if (market_price > zoneh):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.sell('ETCUSD',q7exit,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  sys.exit()
  
elif (market_price < sellsig):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.sell('ETCUSD',q8,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  time.sleep(1)
  
while (market_price > zonel and market_price < buysig):
  time.sleep(1)
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  
if (market_price < zonel):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.buy('ETCUSD',q8exit,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  sys.exit()
  
elif (market_price > buysig):
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])
  myorder = BFX.buy('ETCUSD',q9,market_price,"market")
  print("Order ID: " + str(myorder['order_id']) + " / Price: " + str(myorder['price']) + " / Canceled: " + str(myorder['is_cancelled']) + " / Live: " + str(myorder['is_live']) + " / Order amount: " + str(myorder['original_amount']) + " \n")
  time.sleep(1)
  
  #---------------------------------------------------------------------
  
while (market_price < zoneh and market_price > sellsig):
  time.sleep(1)
  price = BFX.get_ticker('ETCUSD')
  market_price = float(price['last_price'])

orders = BFX.open_order()
#print order[0]['id']
#resp = BFX.cancelOrder(orders[0]['id'])
#print resp
