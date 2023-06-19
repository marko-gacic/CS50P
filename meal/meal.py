def main():
    time = input("What time is it? ")

    breakfastStart = convert("7:00")
    brekfastEnd = convert("8:00")
    lunchStart = convert("12:00")
    lunchEnd = convert("13:00")
    dinnerStart = convert("18:00")
    dinnerEnd = convert("19:00")

    currentTime = convert(time)

    if breakfastStart <= currentTime <= brekfastEnd:
        print("Breakfast Time")
    elif lunchStart <= currentTime <= lunchEnd:
        print("Lunch Time")
    elif dinnerStart <= currentTime <= dinnerEnd:
        print("Dinner Time ")


def convert(time):
    hours, minutes = time.split(':')
    return int(hours) + int(minutes) / 60



if __name__ == "__main__":
    main()