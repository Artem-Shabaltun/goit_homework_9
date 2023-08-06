
ADDRESSBOOK = {}

def input_error (func): # Декоратор - для обробки помилок та виводу повідомлення
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            print("Enter correct username")
        except IndexError:
            print("Give me name and phone please")
        except ValueError:
            print("Enter username")
    return wrapper

def hello_handler(*args):
    return "Hello!"

@input_error
def add_handler(data): #функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} is added"

def exit_handler(*args):
    return "Good bye!"


def command_parser(raw_str): #парсер команд
    elements = raw_str.split()
    for key,value in COMMANDS.items():
        if elements[0].lower() in value:
            return key, elements [1:]
        

def input_error(wrap):
    def inner():
        try:
            result = wrap()
            return result
        except IndexError:
            return "Enter user name"
    return inner


COMMANDS = {
    add_handler: ["add", "додай", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}

def main(): #цикл запит-відповідь
    while True:
        user_input = input(">>>") # add ...
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
