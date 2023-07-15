# if <condition>:
#    <command if is true>
#else:
#    <command if is false>

text = "Apollo et Hyacinthus"

text_list=[]

for letter in text: 
   if  letter not in text_list:
      text_list.append(letter)

print(text_list)