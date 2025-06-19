import timeit
def min_coins_dyn(target):
    for i in range(1, target + 1):
        res.append(float('inf'))
        for j in range(len(coins)):
            if coins[j] <= i:
                if res[i - coins[j]] + 1 < res[i]:
                    res[i] = res[i - coins[j]] + 1
    return backtrack(res, target)


def backtrack(res, t):
    coins_result = {coin: 0 for coin in coins}
    while t > 0:
        coins_left = res[t]
        for coin in coins:
            if res[t - coin] == coins_left - 1:
                coins_result[coin] += 1
                t -= coin
                break
    return {coin: coins_result[coin] for coin in sorted(coins, reverse=True) if coins_result[coin] != 0}


coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 1234
res = [0]
def time_():
    t1 = timeit.default_timer()
    print(min_coins_dyn(target))
    t2 = timeit.default_timer()
    print(t2-t1)

time_()

'Були використані монети: 0.01€, 0.02€, 0.05€, 0.10€, 0.20€, 0.50€, 1.00€, 2.00€'
