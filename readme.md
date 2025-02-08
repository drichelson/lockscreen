# Currency Exchange Rate Phone Lockscreen Image Generator

This project generates a lockscreen image displaying currency exchange rates using Python and the Pillow library. It
takes in 2 [currency codes](https://en.wikipedia.org/wiki/ISO_4217#Active_codes_(list_one)) as arguments and fetches the
exchange rates between them using the [ExchangeRate-API](https://www.exchangerate-api.com/). The exchange rates are then
displayed in a table and saved as a PNG file. The PNG file can be sent to your phone and used as a lockscreen while
traveling.

## Features

- Fetches exchange rates between two currencies.
- Generates an image with convenient exchange rates and saves it as a PNG file.

## Example

<img src="readme_examples/example.png" alt="example" width="300"/>

Screenshot after installing as iPhone lockscreen:

<img src="readme_examples/iphone.jpeg" alt="example" width="300"/>


## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone the repository
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To generate a lockscreen image with exchange rates, run the following command:

```sh
python main.py <home_currency> <foreign_currency>
```
The image is saved in the current directory

Example usage to generate a lockscreen image with exchange rates between USD and VND:

```sh
python main.py USD VND
```

[List of currency codes](https://en.wikipedia.org/wiki/ISO_4217#Active_codes_(list_one)) 
