def battle(x, y):
    import string
    alpha = string.ascii_uppercase

    power_dict = {}
    power = 0
    for i in alpha:
        power += 1
        power_dict[i] = power

    x_power = [power_dict[char] for char in x]
    y_power = [power_dict[char] for char in y]

    if sum(y_power) == sum(x_power):
        return "Tie!"
    elif sum(y_power) > sum(x_power):
        return y
    else:
        return x 
    




