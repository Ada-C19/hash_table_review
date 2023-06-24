from hash_table import HashTable

dict = HashTable()
dict.insert('protagonist', 'Star Butterfly')
dict.insert('comedy relief', 'Glossaryck')
dict.insert('supporting', 'Marco Diaz')
print(dict.arr)

# The "pigeonhole principle" says that if you have 10 pigeonholes and 11 pigeons,
# at least one pigeonhole will have two pigeons. So, if our hash table has 10 slots
# and we insert 11 values, there will necessarily be a collision.
# Also, our hash table isn't a very good one if that happens!
# all_as = ["a" * (i+1) for i in range(7)]
# # print(all_as)
# for i, string in enumerate(all_as):
#     print(f"{i}: {dict.arr}")
#     dict.insert(string, "some_val")