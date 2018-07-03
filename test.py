from coinex import CoinEx, CoinExApiError

# Fill these in
COINEX_ACCESS_ID=''
COINEX_SECRET=''

coinex = CoinEx(COINEX_ACCESS_ID, COINEX_SECRET)

list = coinex.market_list()
print(list)

ticker = coinex.market_ticker('BTCBCH')
print(ticker)

depth = coinex.market_depth('BTCBCH')
print(depth)

deals = coinex.market_deals('BTCUSDT')
print(deals)

balance = coinex.balance()
print(balance)
bch_available = balance['BCH']['available']

wd_list = coinex.balance_coin_withdraw_list()
print(wd_list)

#wd_res = coinex.balance_coin_withdraw('BCH', 'qzjtuuc9nafvfhmwt47z84awltp9gmx7wyma3kvy9v', 0.001)
#print(wd_res)
#wd_id = wd_res['coin_withdraw_id']

#wd_list = coinex.balance_coin_withdraw_list(coin_withdraw_id=wd_id)
#print(wd_list)

#wd_res = coinex.balance_coin_withdraw_cancel(coin_withdraw_id=wd_id)
#print(wd_res)

#od_res = coinex.order_limit('CETBCH', 'sell', 100.0, 10.0)
#print(od_res)
#od_id = od_res['id']

#od_res = coinex.order_pending_cancel('CETBCH', od_id)
#print(od_res)

#od_res = coinex.order_market('CETBCH', 'buy', bch_available)
#print(od_res)
#od_id = od_res['id']

#od_res = coinex.order_status('CETBCH', od_id)
#print(od_res)

#od_res = coinex.order_ioc('CETBCH', 'sell', 100.0, 10.0)
#print(od_res)
#od_id = od_res['id']

od_res = coinex.order_pending('CETBCH')
print(od_res)

od_res = coinex.order_finished('CETBCH')
print(od_res)

#od_id = od_res['data'][0]['id']

#od_res = coinex.order_deals(od_id)
#print(od_res)

od_res = coinex.order_user_deals('CETBCH')
print(od_res)

od_res = coinex.order_mining_difficulty()
print(od_res)

