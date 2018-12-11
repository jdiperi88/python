mylist = [1, 2, 3]
name = 'joey'
list2 = ['joey', 'saida']
# adds something to end of list
mylist.append('saida')

# pops off the item of hte index argument passed in
deletedItem = mylist.pop(0)

# .reverse reverses the list
mylist.reverse()

# if you are adding another list it will spread them across the list you are adding the items to
mylist.extend(list2)
print(name+'s', mylist[-1])

d = {'sam': 1, "joey": 4}
for item in d:
    print(item)
    print(d[item])
