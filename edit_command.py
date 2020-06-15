import csv
from xlrd import open_workbook
from xlutils.copy import copy


def add_to_csv():
    while True:
        input_ticker_adding = input("\nWhat stock's ticker do you want to add to myPortfolio? ")
        input_shares_adding = input("How many shares did you purchased? ")
        input_price_purchase_adding = input("At what price did you purchase it? ")
        print(input_ticker_adding + " | " + input_shares_adding + " | " + input_price_purchase_adding)
        do_add = input("Are you sure you want to add the above to myPortfolio? 'Yes' or 'No'? ")
        if do_add == 'Yes':
            with open("MyPortfolio\MyStocks.csv", "a") as csvfile:
                col_names = ['Ticker', 'Shares', 'Purchase_Price']
                writer = csv.DictWriter(csvfile, fieldnames=col_names)
                writer.writerow({'Ticker': input_ticker_adding,
                                 'Shares': input_shares_adding,
                                 'Purchase_Price': input_price_purchase_adding})
        input_continue = input("Do you want to add more stocks to myPortfolio? 'Yes' or 'No'? ")
        if input_continue == 'No':
            break

def delete_csv_row():
    delete_stock_csv = input("Which stock do you wish to delete from myPortfolio? ")
    lines = list()
    with open('MyPortfolio\MyStocks.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == delete_stock_csv:
                    lines.remove(row)
    with open('MyPortfolio\MyStocks.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

