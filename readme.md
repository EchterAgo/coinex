# coinex

A minimal [coinex.com API](https://github.com/coinexcom/coinex_exchange_api/wiki) wrapper.  Some of the functions accept additional arguments, see the API documentation for those.

## installation

```
pip install coinex.py
```

## usage

```python
from coinex.coinex import CoinEx
from somewhere_else import access_id, secret

coinex = CoinEx(access_id, secret)

# public API
coinex.market_list()
coinex.market_ticker('BCHBTC')
coinex.market_depth('BCHBTC')
coinex.market_deals('BCHBTC')

# private API
coinex.balance_info()
coinex.balance_coin_withdraw_list()
coinex.balance_coin_withdraw('BCH', 'qzjtuuc9nafvfhmwt47z84awltp9gmx7wyma3kvy9v', 0.001)
coinex.balance_coin_withdraw_list(coin_withdraw_id=2465345342)
coinex.balance_coin_withdraw_cancel(coin_withdraw_id=2465345342)
coinex.order_limit('CETBCH', 'sell', 100.0, 10.0)
coinex.order_market('CETBCH', 'buy', 1.0)
coinex.order_ioc('CETBCH', 'sell', 100.0, 10.0)
coinex.order_pending('CETBCH')
coinex.order_finished('CETBCH')
coinex.order_status('CETBCH', 2465345342)
coinex.order_deals(2465345342)
coinex.order_user_deals('CETBCH')
coinex.order_pending_cancel('CETBCH', 2465345342)
coinex.order_mining_difficulty()

#public perpetual API
coinex.perpetual_market_depth(BTCUSDT, 0.1, 20)

#private perpetual API
coinex.perpetual_balance_info()
coinex.perpetual_pending_positions()
coinex.perpetual_order_market(market="BTCUSDT", side=1, amount=0.001)
coinex.perpetual_order_limit(market="BTCUSDT", side=1, amount=0.001, price=18000)
coinex.perpetual_order_cancel(21827192)
coinex.perpetual_order_status(21827192)
```
