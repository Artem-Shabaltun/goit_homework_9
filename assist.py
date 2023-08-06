
ADDRESSBOOK = {}

def add_handler(data): #функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} is added"


def exit_handler(*args):
    return "Good bye!"



def hello_handler(*args):
    return "Hello!"


def command_parser(raw_str): #парсер команд
    items = raw_str.split()
    for key,value in COMMANDS.items():
        if items[0].lower() in value:
            return key, items [1:]


COMMANDS = {
    add_handler: ["add", "додай", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}

def main(): #цикл запит-відповідь
    while True:
        user_input = input(">>>") # add Artem 0957108080
        if not user_input:
            continue
        func, data = command_parser(user_input)
        print(func, data)
        result = func(data)
        print(result)
        if func == exit_handler:
            break
        print(ADDRESSBOOK)
    
if __name__== "__main__":
    main()
