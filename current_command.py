import pandas as pd
import datetime
import matplotlib.pyplot as plt
from colorama import Fore, Style
from get_data import get_stock_data

"""
This section will constitute of
1) Showing the MyPortfolio
2) Showing the graph
3) Intrinsic Value Calculation
4) Calculate the Earnings at the moment
"""


def stock_graph(stock_ticker, stock_data):
    stock_data['Adj Close'].plot()
    plt.title(stock_ticker + " Stock Data")
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()


def stock_graph_MACD(stock_ticker, stock_data):
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.now()
    weekdays = pd.date_range(start=start_date, end=end_date)
    clean_stock_data = stock_data['Adj Close'].reindex(weekdays)
    clean_stock_data = clean_stock_data.fillna(method='ffill')
    exp1 = clean_stock_data.ewm(span=12, adjust=False).mean()
    exp2 = clean_stock_data.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()

    plt.plot(weekdays, macd, label='Short Average', color='blue')
    plt.plot(weekdays, exp3, label='Large Average', color='orange')
    plt.plot()
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)
    plt.title(stock_ticker + " Stock Price and Analytics")
    plt.legend()
    plt.grid()
    plt.show()


# def stock_graph_RSI
def intrinsic_val_calculation(stock_ticker):
    global stock_eps_input, stock_growth_rate_input
    while True:
        try:
            print(Fore.RED + "Warning! The EPS must be positive to do this Intrinsic Value Calculation"
                  + Style.RESET_ALL)
            stock_eps_input = float(input("\nWhat's " + stock_ticker + " EPS? "))
            if stock_eps_input < 0:
                print("Sorry! We can't calculate the intrinsic value with a negative EPS")
            stock_growth_rate_input = float(input("What's " + stock_ticker + " Growth Rate? "))
            break
        except ValueError:
            print("The input must be numbers (Example: '25', '2.5', etc.)")
    pe_ratio = 7
    corp_Bond_Yield = 4.4
    aaa_Bond_Yield = 2.41
    # Basic Graham Intrinsic Value
    # Source: https://www.youtube.com/channel/UCOi_Zu4asFEMKISIbL9yuUA
    graham_intrinsic = (stock_eps_input * (pe_ratio + stock_growth_rate_input) * corp_Bond_Yield) / aaa_Bond_Yield

    # Basic EPS Intrinsic Value
    # Source: https://www.youtube.com/channel/UCOi_Zu4asFEMKISIbL9yuUA
    index_num_years = list(range(0, 4))
    pe_ratio = stock_growth_rate_input * 2
    eps_prediction_list = [stock_eps_input]
    discount_rate = 0.1
    for year in index_num_years:
        eps_prediction_list.append((eps_prediction_list[year] * (1 + stock_growth_rate_input/100)))
    stock_price_prediction_list = [0] * 5
    stock_price_prediction_list[0] = eps_prediction_list[4] * pe_ratio
    index = list(range(1, 5))
    for i in index:
        stock_price_prediction_list[i] = stock_price_prediction_list[i-1]/(1+discount_rate)
    stock_price_prediction_list.reverse()
    eps_intrinsic = stock_price_prediction_list[0]

    # Average of both intrinsic values
    stock_data = get_stock_data(stock_ticker)  # Can put it as a variable in the menu to avoid this step over and over
    intrinsic_value = (eps_intrinsic + graham_intrinsic) / 2
    current_value = stock_data['Adj Close'][stock_data.shape[0] - 1]
    upside = ((intrinsic_value / current_value) - 1) * 100
    return intrinsic_value, upside, current_value


def current_earnings(portfolio_data):
    stocks_tickers_owned_list = portfolio_data['Ticker']
    stocks_purchase_price_owned = portfolio_data['Purchase_Price']
    earnings_percentage_list = []
    earnings_dollars_list = []
    for ticker, shares, purchased_price in zip(stocks_tickers_owned_list, portfolio_data['Shares'],
                                               stocks_purchase_price_owned):
        stock_data = get_stock_data(ticker)  # Can put it as a variable in the menu to avoid this step over again
        current_value = stock_data['Adj Close'][stock_data.shape[0] - 1]
        earnings_percentage_list.append(((current_value / purchased_price) - 1) * 100)
        earnings_dollars_list.append((current_value - purchased_price) * shares)
    return earnings_percentage_list, earnings_dollars_list


def print_earnings(myPortfolio, earnings_percentage_list, earnings_dollars_list):
    print("\nCurrent Earnings:")
    print("Ticker | Total Gain ($) | Total Gain (%)")
    for ticker, percentage, dollars in zip(myPortfolio['Ticker'], earnings_percentage_list,
                                           earnings_dollars_list):
        num_chars_ticker = len(ticker)
        if num_chars_ticker < 5:
            ticker = ticker.rjust(5)
        if dollars < 0:
            print(Fore.RED + ticker + "  |          {:.2f} |    % {:.2f}".format(dollars, percentage) + Style.RESET_ALL)
        else:
            print(Fore.GREEN + ticker + "  |           {:.2f} |     % {:.2f}".format(dollars, percentage)
                  + Style.RESET_ALL)
