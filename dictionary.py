#nama index di dictionary adalah Key
# Urutan pengisian dictionary adalah nama key: value 
d = {'key1': 'item1', 'key2': 'item2', 'kucing':[3,'Jerapah']}

# print(d)
# print(d['key1'])
# print(d['key2'])
# print(d['kucing'])
# print(d['kucing'][1])

# print('kucing' in list(d.keys()))

# for key, val in d.items():
#     print(key)
#     print(val)

# d['key3'] = 'kucing meong'
# del d['key2']

# print(d)
list_lain = ['Buah', 'Kucing', 'Mobil']
dictio = {key:val for val, key in enumerate(list_lain)}
print(dictio)


