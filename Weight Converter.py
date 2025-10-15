weight = int(input('Weight: '))
type = input('(L)bs '.upper() + ' or ' + '(k)g '.upper() )
if type.upper() == "L":
    weight = weight * 0.45
    print(f"You are {weight} kilos")
else:
    weight = weight / 0.45
    print(f"You are {weight} pounds")

    