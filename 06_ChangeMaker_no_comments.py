vals = {
    'quarters': 25,
    'dimes': 10,
    'nickels': 5,
    'pennys': 1
    }

coins = {}

money = input("Enter change to make: \n$")
remainder = 100 * float(money)

for coin, value in vals.items():
    coins[coin] = int(remainder // value)
    remainder %= value

print(coins)
