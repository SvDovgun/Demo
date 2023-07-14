#name = input("Enter  your name: ")
#name_new = name * 3
#print(name_new)

first = 10
second = 5
print((first + second) ** 3)
print((first - second) ** 2)

expression = ((first + second) ** 3 + (first - second) ** 2 ) // 3

print(expression)

#Ви маєте створити наступний вираз. Знайдіть суму чисел first та second, та піднесіть результат до ступеня 3. Також виконайте операцію віднімання first та second, та піднесіть результат до ступеня 2. Отримані результати складіть між собою. Від отриманої суми знайдіть ділення без остачі на 3 та привласніть результат змінній expression

var = None
var_int = 10
var_float = 5.25
var_str = "hello"
var_bool = True

data2 = [1, "python", 3.11] 
print(data2)

data1 = [] 
data1.insert(0, 1)
data1.insert(1, "python")
data1.insert(2, 3.11)
print(data1)

data3 = [1, 3.11]
some_data = ['python']

data3.extend(some_data)
data3.insert(1, "python")
data3.reverse()

print(data3)

data4 = {}
data4["order"] = 1
data4["lang"] = "python"
data4["version"] = 3.11
print(data4)

data = {}
info = {"status": "student", "school": "GoIT"}
data["name"] = "Svit"
data["age"] = 35
data["hobbies"] = ["читаю", "listen music"]
age = data.get("age", 30)
print(age)
data.update(info)
print(data)