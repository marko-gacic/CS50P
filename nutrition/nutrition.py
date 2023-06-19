def main():
    fruit = input("Item: ").lower()

    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        "kiwifruit": 90,
        "pear": 100,
    }

    if fruit in fruit_calories:
        calories = fruit_calories[fruit]
        print(f"Calories: {calories}")
    else:
        print("")

main()