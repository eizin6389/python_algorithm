insert_price = input('insert_price: ')
product_price = input('product_price: ')
change = int(insert_price) - int(product_price)

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ': ' + str(r))
