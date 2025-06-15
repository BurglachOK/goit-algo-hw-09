def find_min_coins(coins, target):
    coins.sort(reverse = True)
    result = {}
    quantity = 0
    for i in range(coins):
        find_min_coins(coins, i)
        













coins = [1, 2, 5, 10, 25, 50, 100, 200]
target = 1234
print(find_min_coins(coins, target))
'Були використані монети: 0.01€, 0.02€, 0.05€, 0.10€, 0.25€, 0.50€, 1.00€, 2.00€'