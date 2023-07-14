"""LIST"""

cars = ["Audi", "Peugeot", "Mercedes" ]
print(type(cars))

print(cars)

cars.append("BMW")

print(cars)

print(cars[2])

cars[1] = "Hyundai"

print(cars)

cars.insert(1, "Subaru")

print(cars)
print(len(cars))

pop_value = cars.pop()
print("pop_value " + pop_value)
print(cars)

cars.reverse()
print(cars)