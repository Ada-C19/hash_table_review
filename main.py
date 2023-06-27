from hash_table import HashTable

dict = HashTable()
dict.insert('protagonist', 'Star Butterfly')
print(dict.arr)
# dict.insert('protagonist', 'Star Butterfly2')
# print(dict.arr)

print(dict.get('protagonist'))

all_as = ['a' * i for i in range(10)]
print(all_as)
for a in all_as:
    dict.insert(a, 'some_val')

print(dict.get('protagonist'))
print(dict.get('aaaa'))