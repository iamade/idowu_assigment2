def profit(prices):
    min_price_so_far, max_profit = float('inf'), 0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(price, min_price_so_far)
    return max_profit

# prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
print(profit(prices))
