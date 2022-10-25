from typing import Dict
from classes import RequestHandler
import requests

__all__ = ["Client"]


class Client:
    DEFAULT_TIMEOUT = 10
    ABAN_API_URL = 'https://abantether.com/api/'
    VERSION = 'v1/'
    BASE_URL = ABAN_API_URL + VERSION
    # OTC addresses
    BUY_ORDER_URL = 'otc/orders/buy/'
    SELL_ORDER_URL = 'otc/orders/sell/'
    SELL_ALL_ORDER_URL = 'otc/orders/sell/all/'
    SELL_ALL_ORDER_VERIFY_URL = 'otc/orders/sell/all/verify/'
    CANCEL_ORDER_URL = 'otc/orders/cancel/'
    CANCEL_STOP_ORDER_URL = 'otc/orders/cancel/stop-loss/'
    COIN_INFO_URL = 'otc/coin-info/'
    # USERS addresses
    BALANCE_URL = 'users/balance/'
    WHITE_ADDRESS_URL = 'users/white-address/list/'
    DEPOSIT_CRYPTO_URL = 'users/deposit/crypto/'
    WITHDRAW_CRYPTO_URL = 'users/withdraw/crypto/'
    FEE_URL = 'users/fee/'
    COINS_URL = 'users/coins/'
    NETWORKS_URL = 'users/networks/'
    WALLETS_URL = 'users/wallets/'

    def __init__(self, api_key: str, timeout: int = None):
        self._request = RequestHandler(base_url=self.BASE_URL, api_key=api_key, timeout=timeout)

    def buy_order(self):
        self._request.post(url=self.BUY_ORDER_URL)

    def get_buy_orders(self):
        self._request.get(url=self.BUY_ORDER_URL)

    def sell_order(self):
        self._request.post(url=self.SELL_ORDER_URL)

    def cancel_order(self):
        self._request.post(url=self.CANCEL_ORDER_URL)

    def cancel_stop_order(self):
        self._request.post(url=self.CANCEL_STOP_ORDER_URL)

    def get_coin_info(self):
        self._request.post(url=self.COIN_INFO_URL)

    def get_sell_orders(self):
        self._request.post(url=self.SELL_ORDER_URL)

    def sell_all_orders(self):
        self._request.post(url=self.SELL_ALL_ORDER_URL)

    def verify_sell_all_orders(self):
        self._request.post(url=self.SELL_ALL_ORDER_VERIFY_URL)

    def deposit_crypto(self):
        self._request.post(url=self.DEPOSIT_CRYPTO_URL)

    def withdraw_crypto(self):
        self._request.post(url=self.WITHDRAW_CRYPTO_URL)

    def get_deposit_crypto_list(self):
        self._request.get(url=self.DEPOSIT_CRYPTO_URL)

    def get_withdraw_crypto_list(self):
        self._request.get(url=self.WITHDRAW_CRYPTO_URL)

    def get_fee(self):
        self._request.get(url=self.FEE_URL)

    def get_coins(self):
        self._request.get(url=self.COINS_URL)

    def get_networks(self):
        self._request.get(url=self.NETWORKS_URL)

    def get_wallets(self):
        self._request.get(url=self.WALLETS_URL)

    def get_white_addresses(self):
        self._request.get(url=self.WITHDRAW_CRYPTO_URL)

    def get_balance(self):
        self._request.get(url=self.BALANCE_URL)
