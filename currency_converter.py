
def get_amount():
    while True:
        try:
            amount: float = float(input("Enter the amount: "))

            if amount < 1:
                raise ValueError
        
            return amount

        except ValueError:
            print("Invalid amount!")

def get_currency(label: str):
    CURRENCIES = ("USD", "EUR", "CAD")

    while True:
        currency = input(f"{label} currency (USD/EUR/CAD): ").upper()

        if currency not in CURRENCIES:
            print("Invalid currency!")
        
        return currency

def convert(amount, source, target):
    exchange_rates = {
        'USD': {'EUR': 0.85, 'CAD': 1.25},
        'EUR': {'USD': 1.18, 'CAD': 1.47},
        'CAD': {'EUR': 0.68, 'USD': 0.80},
    }

    if source == target:
        return amount

    return amount * exchange_rates[source][target]


def main():
    amount = get_amount()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")

    converted_amount = convert(amount, source_currency, target_currency)
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f}")


if __name__ == '__main__':
    main()