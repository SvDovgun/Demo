names = ["Bill", "Gill", "Marry"]
ages = range(18, 90)

count_marry = 0

#for _ in range(3):
while True:
    name = input("name >>>")
    age = int(input("age >>>"))

    if age in ages and name in names: 
        print("welcome to party")
        if count_marry > 3:
            break
        if name == "Marry":            
            count_marry += 1
            continue
    elif age >= 90:
        print("to old")
    else:
        print("too young")

    #if name == "Marry":
    #    break
    names.pop(names.index(name))

print(names)
