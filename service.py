from model import get_item,add_item,update_items,delete_items,get_item_with_type,get_all_items

def getitemsbyid(id):
    return get_item(id)

def getallitems():
    return get_all_items()

def getitemsbytype(type):
    return get_item_with_type(type)

def additems(data):
    id=data.id
    name=data.name
    price=data.price
    quantity=data.quantity
    type=data.type
    return add_item(id,name,price,quantity,type)

def updateitems(id,data):
    price=data.price
    quantity=data.quantity
    return update_items(id,price,quantity)

def deleteitem(id):
    return delete_items(id)