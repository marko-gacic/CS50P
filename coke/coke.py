def calculate_change(coin_sum):
    return coin_sum - 50

def coke_machine():
    coin_sum = 0
    print("Amount Due: 50 ")
    while coin_sum < 50:
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            coin_sum += coin
        print("Amount Due:", 50 - coin_sum)

    change = calculate_change(coin_sum)
    print("Change Owed:", change)

coke_machine()
