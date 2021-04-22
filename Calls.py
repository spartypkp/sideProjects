import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


class Call(object):
    name = "NA"
    ticker = ""
    strike_price = 0
    original_premium = 0
    expiration_days = 0
    premium = 0
    share_price = 0

    def future_value(self, new_price, new_premium):
        total_cost = (self.strike_price * 100)
        revenue = (new_price * 100)
        profit = revenue - total_cost
        return profit

    def __init__(self, strike_price, premium, expiration_days, name, ticker, share_price):
        self.strike_price = strike_price
        self.original_premium = premium
        self.expiration_days = expiration_days
        self.name = name
        self.ticker = ticker
        self.share_price = share_price


def main():

    # Strike price remains constant
    style.use('ggplot')

    start = dt.datetime(2015, 1, 1)
    end = dt.datetime.now()
    df = web.DataReader("TSLA", 'morningstar', start, end)
    print(df)
    """
    Delta = Call(31.0, 4.88, 155, "Delta Air Lines", "DAL", 31.31)
    futures = [(35, 5.2),(40, 5.2),(45, 5.2),(50, 5.2),(55, 5.2),(60, 5.2),(65, 5.2),(70, 5.2)]
    profits = []
    for tup in futures:
        profit = Delta.future_value(tup[0],tup[1])
        print("DAL:   Price(",tup[0],")  Premium(",tup[1],") will produce a profit of:", profit)
    """

main()