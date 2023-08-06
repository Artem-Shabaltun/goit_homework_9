
def add_handler(*args): #функції обробники команд
    return args


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
    hello_handler: ["Hello"]
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
    
if __name__== "__main__":
    main()
