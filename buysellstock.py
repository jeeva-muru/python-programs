# description: Given an array of stock prices, find the best day to buy and 
# sell the stock to maximize profit.

def buysellstock(prices):
    max_profit = 0
    min_price = min(prices)
    buy_day = prices.index(min_price)
    # for i in range(1, len(prices)):
    #     if prices[i] > prices[i-1]:
    #         max_profit += prices[i] - prices[i-1]
    
    # print(max_profit)
    sell_day=0
    for i in range(buy_day, len(prices)):
        # print("i", i )
        # print("max",max_profit)
        if (prices[i] - prices[buy_day]) > max_profit:
            max_profit = prices[i]- prices[buy_day]
            # print("loop",i)
            sell_day = i

    # print(max_profit)    
    
    print("buy_day", buy_day+1)
    print("sell_day", sell_day+1)

# array of stock prices
# index represents the day
# value represents the price of the stock 
prices = [7,1,5,3,6,4]

print(buysellstock(prices))
