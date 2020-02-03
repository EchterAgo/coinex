import hashlib
import time
import requests
import collections

class CoinExApiError(Exception):
    pass

class CoinEx:
    _headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }

    def __init__(self, access_id=None, secret=None):
        self._access_id = access_id
        self._secret = secret

    def currency_rate(self):
        return self._v1('common/currency/rate')

    def asset_config(self, **params):
        return self._v1('common/asset/config', **params)

    def market_list(self):
        return self._v1('market/list')

    def market_ticker(self, market):
        return self._v1('market/ticker', market=market)

    def market_ticker_all(self):
        return self._v1('market/ticker/all')

    def market_depth(self, market, merge='0.00000001', **params):
        return self._v1('market/depth', market=market, merge=merge, **params)

    def market_deals(self, market, **params):
        return self._v1('market/deals', market=market, **params)

    def market_kline(self, market, type='1hour', **params):
        return self._v1('market/kline', market=market, type=type, **params)

    def market_info(self):
        return self._v1('market/info')

    def market_detail(self, market):
        return self._v1('market/detail', market=market)

    def margin_market(self):
        return self._v1('margin/market')

    def margin_transfer(self, from_account, to_account, coin_type, amount):
        return self._v1('margin/transfer', method='post', auth=True, from_account=from_account, to_account=to_account, coin_type=coin_type, amount=amount)

    def margin_account(self, **params):
        return self._v1('margin/account', auth=True, **params)

    def margin_config(self, **params):
        return self._v1('margin/config', auth=True, **params)

    def margin_loan_history(self, **params):
        return self._v1('margin/loan/history', auth=True, **params)

    def margin_loan(self, market, coin_type, amount):
        return self._v1('margin/loan', method='post', auth=True, market=market, coin_type=coin_type, amount=amount)

    def margin_flat(self, market, coin_type, amount, **params):
        return self._v1('margin/flat', method='post', auth=True, market=market, coin_type=coin_type, amount=amount, **params)

    def future_market(self):
        return self._v1('future/market')

    def future_transfer(self, from_account, to_account, coin_type, amount):
        return self._v1('future/transfer', method='post', auth=True, from_account=from_account, to_account=to_account, coin_type=coin_type, amount=amount)

    def future_account(self, **params):
        return self._v1('future/account', auth=True, **params)

    def future_limitprice(self, account_id):
        return self._v1('future/limitprice', account_id=account_id)

    def future_config(self, **params):
        return self._v1('future/config', auth=True, **params)

    def future_loan_history(self, account_id, **params):
        return self._v1('future/loan/history', auth=True, account_id=account_id, **params)

    def future_loan(self, account_id, coin_type, amount):
        return self._v1('future/loan', method='post', auth=True, account_id=account_id, coin_type=coin_type, amount=amount)

    def future_flat(self, account_id, coin_type, amount, **params):
        return self._v1('future/flat', method='post', auth=True, account_id=account_id, coin_type=coin_type, amount=amount, **params)

    def option_market(self):
        return self._v1('option/market')

    def option_detail(self):
        return self._v1('option/detail')

    def option_issue(self, market_type, amount):
        return self._v1('option/issue', method='post', auth=True, market_type=market_type, amount=amount)

    def option_redeem(self, market_type, amount):
        return self._v1('option/redeem', method='post', auth=True, market_type=market_type, amount=amount)

    def balance_info(self):
        return self._v1('balance/info', auth=True)

    def balance_coin_withdraw_list(self, **params):
        return self._v1('balance/coin/withdraw', auth=True, **params)

    def balance_coin_withdraw(self, coin_type, coin_address, actual_amount, transfer_method, **params):
        return self._v1('balance/coin/withdraw', method='post', auth=True, coin_type=coin_type, coin_address=coin_address, actual_amount=actual_amount, transfer_method=transfer_method, **params)

    def balance_coin_withdraw_cancel(self, coin_withdraw_id, **params):
        return self._v1('balance/coin/withdraw', method='delete', auth=True, coin_withdraw_id=coin_withdraw_id, **params)

    def balance_coin_deposit_list(self, **params):
        return self._v1('balance/coin/deposit', auth=True, **params)

    def balance_deposit_address(self, coin_type, **params):
        return self._v1('balance/deposit/address/{}'.format(coin_type), auth=True, **params)

    def balance_deposit_address_new(self, coin_type, **params):
        return self._v1('balance/deposit/address/{}'.format(coin_type), method='post', auth=True, **params)

    def sub_account_transfer(self, coin_type, amount, **params):
        return self._v1('sub_account/transfer', auth=True, coin_type=coin_type, amount=amount, **params)

    def order_limit(self, market, type, amount, price, **params):
        return self._v1('order/limit', method='post', auth=True, market=market, type=type, amount=amount, price=price, **params)

    def order_market(self, market, type, amount, **params):
        return self._v1('order/market', method='post', auth=True, market=market, type=type, amount=amount, **params)

    def order_ioc(self, market, type, amount, price, **params):
        return self._v1('order/ioc', method='post', auth=True, market=market, type=type, amount=amount, price=price, **params)

    def order_pending(self, market, page=1, limit=100):
        return self._v1('order/pending', method='get', auth=True, market=market, page=page, limit=limit)

    def order_finished(self, market, page=1, limit=100):
        return self._v1('order/finished', method='get', auth=True, market=market, page=page, limit=limit)

    def order_status(self, market, id):
        return self._v1('order/status', method='get', auth=True, market=market, id=id)

    def order_deals(self, id, page=1, limit=100):
        return self._v1('order/deals', method='get', auth=True, id=id, page=page, limit=limit)

    def order_user_deals(self, market, page=1, limit=100):
        return self._v1('order/user/deals', method='get', auth=True, market=market, page=page, limit=limit)

    def order_pending_cancel(self, market, id):
        return self._v1('order/pending', method='delete', auth=True, market=market, id=id)

    def order_pending_cancel_all(self, account_id, market):
        return self._v1('order/pending', method='delete', auth=True, account_id=account_id, market=market)

    def order_mining_difficulty(self):
        return self._v1('order/mining/difficulty', method='get', auth=True)

    def _v1(self, path, method='get', auth=False, **params):
        headers = dict(self._headers)

        if auth:
            if not self._access_id or not self._secret:
                raise CoinExApiError('API keys not configured')

            params.update(access_id=self._access_id)
            params.update(tonce=int(time.time() * 1000))

        params = collections.OrderedDict(sorted(params.items()))

        if auth:
            headers.update(Authorization=self._sign(params))

        if method == 'post':
            resp = requests.post('https://api.coinex.com/v1/' + path, json=params, headers=headers)
        else:
            fn = getattr(requests, method)
            resp = fn('https://api.coinex.com/v1/' + path, params=params, headers=headers)

        return self._process_response(resp)

    def _process_response(self, resp):
        resp.raise_for_status()

        data = resp.json()
        if data['code'] is not 0:
            raise CoinExApiError(data['message'])

        return data['data']

    def _sign(self, params):
        data = '&'.join([key + '=' + str(params[key]) for key in sorted(params)])
        data = data + '&secret_key=' + self._secret
        data = data.encode()
        return hashlib.md5(data).hexdigest().upper()
