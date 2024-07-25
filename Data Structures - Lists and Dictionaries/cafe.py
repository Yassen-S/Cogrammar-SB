menu = ["coffee", "Tea", "Cake", "Buiscuit"]

stock = {"coffee" : 10, "Tea" : 10, "Cake" : 15, "Buiscuit" : 20}

price = {"coffee" : 2.20, "Tea" : 1.50, "Cake" : 2.50, "Buiscuit" : 0.80}

total_stock = 0

for item_stock in stock:
    item_value = (stock[item_stock] * price[item_stock])
    total_stock += item_value
    print(f"The total value of stock for {item_stock} is £{item_value}")

print(f"The total value of all stock is: £{total_stock}")