while 1:
    name, age, weight = input().split()
    if name == "#":
        break
    else:
        print(f'{name} Senior') if (int(age) > 17 or int(weight) >= 80) else print(f'{name} Junior')