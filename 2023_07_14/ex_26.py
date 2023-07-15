#print(print("Hello"))
verdi = ["Attila", "Nabucco", "Macbeth", "Rigoletto", "La traviata", "Don Carlos", "Otello"]

def custom_print(a):
    #print(f"Opera {a}")
    return f"Opera {a}"

#for opera in verdi:
#    custom_print(opera)
#    #print(custom_print(opera))

result_list = []

for opera in verdi:
    result_list.append(custom_print(opera))

print(result_list)