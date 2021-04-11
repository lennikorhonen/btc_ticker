from fetch import get_price


def main():
    print('Prices:')
    prices = get_price()
    print('Time:', prices['time']['updated'])
    print('BTC in EUR:', prices['bpi']['EUR']['rate_float'])


if __name__ == '__main__':
    main()