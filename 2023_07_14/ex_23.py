# for

text = "Apollo et Hyacinthus"

for letter in text: 
    print(letter, end=" ")

text_list=[]

for letter in text: 
   text_list.append(letter)

print(text_list)

print(text_list.count("h"))

verdi = ["Attila", "Nabucco", "Macbeth", "Rigoletto", "La traviata", "Don Carlos", "Otello"]

for i in verdi:
    print(i)