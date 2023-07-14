"""Dictionary"""

cars = {"premium": ["Mercedes", "Audi", "BMW"], "economy": ["Renault", "Citroen"]}

print(type(cars))

print(cars)
print(cars["premium"])
print(cars["premium"][1])
print(cars["premium"] + cars["economy"])

result = cars.get("1")
print(result)

result = cars.get("economy")
print(result)

cars[1] = ["Subary", "Citroen"]
print(cars)

cars[1] += ["New Brend", "new brend 2"]
print(cars)

cars.update({3: "Smart"})

print(cars.pop(1))

print(cars)