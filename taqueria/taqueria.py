menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def order():
    order_total = 0.0
    try:
        while True:
            item = input("Item: ").title()
            if not item:
                break
            if item in menu:
                price = menu[item]
                order_total += price
                print(f"Total: ${order_total:.2f}")
            else:
                print("Invalid item")
    except EOFError:
        pass
    print(f"Total is ${order_total:.2f}")

order()