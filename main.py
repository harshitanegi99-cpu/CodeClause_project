#Showing all the exchange rates:
exchange_rates ={
    "USD": 1.0,  #Base Currrency
    "INR": 82.06,
    "CNY": 7.112,
    "JPY": 147.83,
    "MYR": 4.2200,
    "SGD": 1.2842,
    "EUR": 0.85,
    "GBP": 0.79,
    "AUD": 1.55,
    "CAD": 1.36,
}
#Defining a function for converting the currency:
def convert_currency( amount, from_currency , to_currency ):
    if from_currency not in  exchange_rates or  to_currency not in exchange_rates:
        raise ValueError("Ivalid currency code")
    
    # Convert amount to USD first:
    amount_in_usd = amount / exchange_rates[from_currency]
 
# Convert from USD to the target currency:
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    print(converted_amount)

amount= float(input("Enter the amount to convert:"))
from_currency=  (input("Enter the currency to convert from (e.g., USD,EUR):")).upper()
to_currency=  (input("Enter the currency to convert  to (e.g., USD,EUR):")).upper()

convert_currency( amount, from_currency , to_currency)