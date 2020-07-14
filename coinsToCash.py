def calc_dollars(**coins):
    sum = 0

    for (key, value) in coins.items():
        if key == "pennies":
            sum += value*.01
            # print(sum)
        elif key == "nickels":
            sum += value*0.05
            # print(sum)
        elif key == "dimes":
            sum += value*0.10
            # print(sum)
        elif key == "quarters":
            sum += value*0.25
            print(f"${sum}")


calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)
