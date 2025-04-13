Products = {'Books': 200, 'T-shirt': 500, 'Watch': 1000, 'Mobile': 2000, 'Shoes': 1000}

for product, price in Products.items():
    print(f"{product} --> ₹{price}")

quantities = {}

for item in Products:
    while True:
        try:
            itm = int(input(f"Enter the quantity {item} "))
            if itm < 0:
                print("quantity should not be negative ")
                continue
            quantities[item] = itm
            break
        except ValueError:
            print("quantity should be numeric ")


for product, quantity in quantities.items():
    print(f"{product} --> {quantity}")

final_amt = 0

for prod in quantities:
    prod_qty = quantities[prod]
    prod_price = Products[prod]
    total_amount = prod_qty * prod_price
    final_amt += total_amount


def get_discount(ord_amt):
    if ord_amt >= 5000:
        return ord_amt * 0.10
    elif (ord_amt >= 2500) and (ord_amt < 5000):
        return ord_amt * 0.05
    else:
        return ord_amt * 0.0


discount = get_discount(final_amt)
print(f"Total price. Rs {final_amt} ")
print(f"final price after discount {final_amt-discount}")
print(f"discount is {discount}")