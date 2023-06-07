products = ["Sankofa Foods" , "Jamestown Coffee" , "Bioko Chocolate" , "Blue Skies Ice Cream",
            "fair Afric Chocolate" , "Kawa Moka Coffee" , "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

## Total Price Average for all Products

total_prices = sum(prices)
average_prices = total_prices / len(prices)

print(average_prices)

# A new price list with the prices reduced by $5

reduced_prices = [price - 5 for price in prices]

print(reduced_prices)

# Total Revenue Generated from the Products

total_revenue = sum(price * quantity for price, quantity in zip(prices, last_week))
print(total_revenue)

#Average daily Revenue from the Products 

average_daily_revenue = total_revenue / len(prices)
print(average_daily_revenue)

# Products costing less than $30

for price in prices:
    if price < 30:
        print(price)
        