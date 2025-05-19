def round_half_up(number, decimals: int):
    rounded_value = int(number * (10**decimals) + 0.5) / (10**decimals)

    if rounded_value % 1 == 0:
        rounded_value = int(rounded_value)

    return rounded_value

print(round_half_up(float(input("Number: ")), 3))