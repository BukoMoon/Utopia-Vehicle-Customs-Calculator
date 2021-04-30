from datetime import datetime


def calculate(price: int, year: int, category: str) -> float or str:
    # Uses the datetime library to get current year for calculation
    current_year = datetime.now().year
    # Conditional statement tests
    if category == 'A':
        percentage = 0.25
    elif category == 'B':
        percentage = 0.5
    else:
        percentage = 0.75

    initial_amount = percentage * price
    year_difference = current_year - year
    # Depreciation amount is equal 1% of the price times by how many years old.
    depreciation_amount = year_difference * (0.01 * price)

    # Conditional statement tests if the depreciation is greater than 10%
    if depreciation_amount >= (0.1 * price):
        depreciation_amount = 0.1 * price
    final_amount = initial_amount - depreciation_amount
    return category, initial_amount, year_difference, depreciation_amount, final_amount


def repeat_process(stop):
    # To loop dialog if an unexpected input is entered.
    while True:
        # Asking user if they wish to continue
        answer = input('Calculate for another vehicle (y/n)? ')
        # Conditional statement checks user input, while loop breaks if the user input is 'y' or 'n'
        if 'n' in answer.lower():
            print('Have a nice day!')
            stop = True
            break
        elif 'y' in answer.lower():
            print('-' * 40)
            break
        else:
            print('Unexpected input. Please try again.')
    return stop


if __name__ == '__main__':
    # Initialising main loop
    end = False
    while not end:
        print('Utopia Vehicle Customs Calculator')
        print('-' * 40)

        # Asking for user input for initial values.
        market_price = int(input('Enter the market price: '))
        engine_capacity = int(input('Enter the engine capacity: '))
        manufacturer_year = int(input('Enter the manufacture year: '))

        # Conditional statement checks the engine capacity for which category should be used.
        if engine_capacity <= 1600:
            tier, initial, year_diff, depreciation, final = calculate(market_price, manufacturer_year, 'A')
        elif 2000 > engine_capacity > 1600:
            tier, initial, year_diff, depreciation, final = calculate(market_price, manufacturer_year, 'B')
        elif engine_capacity >= 2000:
            tier, initial, year_diff, depreciation, final = calculate(market_price, manufacturer_year, 'C')

        # Displays information returned from the calculate function
        print(f'Initial customs amount (Category {tier}): ${initial:,.2f}')
        print(f'Depreciation discount ({year_diff} years): ${depreciation:,.2f}')
        print(f'Final customs amount: ${final:,.2f}')

        end = repeat_process(end)
