from collections import namedtuple

import requests


def get_exchange_rate(home, foreign):
    """
    Gets the exchange rate between two currencies.
    Returns 2 values: the exchange rate from home to foreign, and the exchange rate from home to USD.
    """
    # this api is updated daily and requires no authentication:
    response = requests.get('https://open.er-api.com/v6/latest/' + home)
    response_json = response.json()
    return response_json['rates'][foreign], response_json['rates']['USD']


def format_currency(value):
    """
    Formats a currency value to a string. Only displays a decimal place if the value is less than 5.
    """
    if value < 5:
        return f"{value:.1f}".rstrip('0').rstrip('.')
    else:
        return f"{value:,.0f}"


def create_rows(header_row, home_to_foreign_rate, home_to_usd_rate):
    """
    Creates a list of convenient currency conversions. Each row contains a 2-tuple of foreign currency value and the home currency value.
    The table is sorted by the USD value, and duplicates are removed. header_row is inserted at the beginning of the list.
    """
    interesting_values = [1, 5, 10, 20, 50, 100, 500, 1000, 10000, 100000, 500000, 1000000, 10000000]
    unfiltered_rows = []
    foreign_to_home_rate = 1 / home_to_foreign_rate

    # we track usd alongside foreign and home values for filtering purposes:
    row = namedtuple('row', ['foreign', 'home', 'usd'])

    # append all possible interesting values:
    for v in interesting_values:
        unfiltered_rows.append(row(v, v * foreign_to_home_rate, v * foreign_to_home_rate * home_to_usd_rate))
        unfiltered_rows.append(row(v * home_to_foreign_rate, v, v * home_to_usd_rate))

    # remove all rows below 1 USD and above 100 USD:
    unfiltered_rows = list(filter(lambda x: 1 <= x.usd <= 100, unfiltered_rows))

    # sort by usd value:
    unfiltered_rows.sort(key=lambda x: x.usd)

    # format usd with appropriate rounding so we can dedupe similar values:
    unfiltered_rows = list(map(lambda x: row(x.foreign, x.home, format_currency(x.usd)), unfiltered_rows))

    # dedupe usd fields:
    filtered_rows = []
    for v in unfiltered_rows:
        if len(filtered_rows) == 0 or filtered_rows[-1].usd != v.usd:
            filtered_rows.append(v)

    # format fields, dropping the usd field:
    formatted_rows = list(map(lambda x: (format_currency(x.foreign), format_currency(x.home)), filtered_rows))

    formatted_rows.insert(0, header_row)
    return formatted_rows
