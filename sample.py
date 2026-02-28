data=[(1, 'Apple', 30, 50, 'Fruits'), (2, 'Mango', 90, 10, 'Fruits')]
list_items=[]
items={}

for i in data:
    items["id"] = i[0]
    items["name"] = i[1]
    items["price"] = i[2]
    items["quantity"] = i[3]
    items["type"] = i[4]
    list_items.append(items)

    
print(items)
print()
print(list_items)