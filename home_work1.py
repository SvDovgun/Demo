#На лекції ми з вами розглянули цикл while та функцію input. Також дізналися про одну з колекцій - список, і про деякі методи роботи з ним. Тож, використовуючи ці знання, ми з вами виконаємо перше ДЗ

#Створити змінну з типом list (ім’я на ваш розсуд).
#Наповнити цю змінну даними. Використати input в циклі while.
#Умовою для завершення циклу while має бути перевірка довжини змінної списку (використаємо функцію len())
#У ній має бути не менше 10 елементів.

#Після наповнення списку і завершення циклу while - роздрукувати вміст списку, об’єднавши всі елементи в один рядок за допомогою метода join. Роздільником має бути символ “;”.

read_books= []
#print(type(read_books))
list_lenght = len(read_books)

while list_lenght < 10:
    element = input("Enter read book name>>> ")
    read_books.append(element)
    list_lenght = len(read_books)

print(f'{"; ".join(read_books)}')