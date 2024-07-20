def printTransactions(m, k, d, names, owned, prices):
    transactions = []
    
    # Simple strategy: Sell stocks that have increased in price, buy those that have decreased
    for i in range(k):
        stock_name = names[i]
        stock_owned = owned[i]
        stock_prices = prices[i]
        
        current_price = stock_prices[-1]
        previous_price = stock_prices[-2]
        
        # Check if we should sell
        if stock_owned > 0 and current_price > previous_price:
            transactions.append(f"{stock_name} SELL {stock_owned}")
        
        # Check if we should buy
        if m >= current_price and current_price < previous_price:
            num_to_buy = int(m // current_price)
            if num_to_buy > 0:
                transactions.append(f"{stock_name} BUY {num_to_buy}")
                m -= num_to_buy * current_price
    
    # Output the transactions
    print(len(transactions))
    for transaction in transactions:
        print(transaction)

def main():
    # Read first line of input
    first_line = input().strip().split()
    m = float(first_line[0])
    k = int(first_line[1])
    d = int(first_line[2])
    
    # Initialize lists for names, owned stocks, and prices
    names = []
    owned = []
    prices = []
    
    # Read each stock's data
    for _ in range(k):
        stock_data = input().strip().split()
        names.append(stock_data[0])
        owned.append(int(stock_data[1]))
        prices.append([float(price) for price in stock_data[2:]])
    
    # Call the printTransactions function with the gathered input
    printTransactions(m, k, d, names, owned, prices)

# Example usage
main()
