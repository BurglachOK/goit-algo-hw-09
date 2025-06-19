def find_coins_greedy(coins, target):
    coins.sort(reverse = True)
    result = {}
    quantity = 0

    for i in coins:
        while i <= target:
            target -= i
            quantity += 1
            result[i] = quantity
        quantity = 0
    return result

    


coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 1234
print(find_coins_greedy(coins, target))
'Були використані монети: 0.01€, 0.02€, 0.05€, 0.10€, 0.20€, 0.50€, 1.00€, 2.00€'
