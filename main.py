import argparse

import lockscreen
from currency import get_exchange_rate, create_rows

# Create the parser
parser = argparse.ArgumentParser(description='Process two currency codes.')

# Add arguments
parser.add_argument('home_currency', type=str, help='The home currency code')
parser.add_argument('foreign_currency', type=str, help='The foreign currency code')

# Parse the arguments
args = parser.parse_args()

# Access the arguments
home_currency = args.home_currency
foreign_currency = args.foreign_currency

home_to_foreign_rate, home_to_usd_rate = get_exchange_rate(home_currency, foreign_currency)
table_data = create_rows((foreign_currency, home_currency), home_to_foreign_rate, home_to_usd_rate)
lockscreen.create_image(table_data, home_currency + foreign_currency + ".png")
