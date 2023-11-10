
# My proyect CRUD -> Generar, actualizar, eliminar, buscar 
clients = ['andres', 'alexander', 'chaparro']


def create_cliente(client):
    global clients
    if client_name not in clients:  # what the client not found
        clients.append(client_name)
    else:
        print("clients already exist {}".format(client_name))


def read_client():
    global clients
    if client_name in clients:
        print("Find user")
        for idx, client in enumerate(clients,1):
            print('{}:{}'.format(idx, client))
    else:
        print("not find user")

def update_client(client_name, new_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = new_name
        print(f"Updated {client_name} to {new_name}")
    else:
        print("Client not found")


def delete_client():
    global clients
    if client_name in clients:
        # Remove the client name and the trailing comma
        clients.remove(client_name)
        print(f"Deleted {client_name}")
    else:
        print("Client not found")

def _print_welcome():
    print("WELCOME UNIVERSIDAD DEL VALLE -TULUÁ")
    print('*' * 90)
    print("What would you like to do today:")
    print("[C]reate Client o user:")
    print("[R]read Client o user:")
    print("[U]pdate Client o user:")
    print("[D]elete Client o user:")


def get_client_name():  # la funcion me permite preguntar por el nombre del cliente
    return input("type your name client: ")


def get_list_client_names():
    global clients
    print(clients)


if __name__ == '__main__':
    _print_welcome()
    # poner en mayuscula (.upper())
    option = input("type option desired client: ").upper()

    if option == 'C':
        client_name = get_client_name()
        create_cliente(client_name)
        get_list_client_names()
    elif option == 'R':
        client_name = get_client_name()
        read_client()
        get_list_client_names()
    elif option == 'U':
        client_name = get_client_name()
        new_name = str(input("enter the new name to update: "))
        update_client(client_name, new_name)
        get_list_client_names()
    elif option == 'D':
        client_name = get_client_name()
        delete_client()
        get_list_client_names()
    else:
        print("command invalid")