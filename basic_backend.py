import mvc_exceptions as mvc_exc

items = list() #Variables globales donde estarán almacenada la información

def create_items(app_items): #Metodo que accede a los datos de la varible global
    global items
    items = app_items
    
def create_item(name, price, quantity): #Metodo que crea items pidiendo 3 características
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored'.format(name))
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})
    
def read_item(name): #Busca y lee un item con un nombre en específico
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:             #En caso de no encontrarlo muestra un mensaje
        raise mvc_exc.ItemNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(name))

def read_items(): #Lee item por item 
    global items
    return [item for item in items]

def update_item(name, price, quantity): #Actualizar los items que ya están creados
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(name))
        
def delete_item(name): #Elimina un registro
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t delete "{}" because it\'s not stored'.format(name))

def main():
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]
    
    #Create
    create_items(my_items)
    create_item('beer', price= 3.0, quantity= 15)
    #Aqui si queremos crear un item que ya tenemos se obtiene el mensaje de que ya esta creado
    
    #Read
    print('READ items')
    print(read_items())
    #Si queremos leer un item que no tenemos almacenado recibimos el mensaje acorde
    print('READ bread')
    print(read_item('bread'))
    
    #Update
    print('UPDATE bread')
    update_item('bread', price = 2.0, quantity = 30)
    print(read_item('bread'))
    #En caso de querer actualizar un item inexistente obtenemos el mensaje de que no está almacenado
    
    #Delete
    print('DELETE beer')
    delete_item('beer')
    #Si el item no está en le registro se obtiene el mensaje diciendo que no se puede completar 
    
    print('READ items')
    print(read_items)
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    