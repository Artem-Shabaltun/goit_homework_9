
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

def sanitize_contacts(phone_num):
    new_phone = (
        phone_num.strip()
        .removeprefix("+")
        .replace("(","")
        .replace(")","")
        .replace("-","")
        .replace(" ","")
    )
    return new_phone

def hello_handler(*args):
    return "Hello! How can I help you?"

@input_error
def add_handler(name, phone_num): # Додаємо контакт в список. Приклад: "add User_name 095-xxx-xx-xx"
    if name in ADDRESSBOOK:
        ADDRESSBOOK[name].append(sanitize_contacts(phone_num))
    if name not in ADDRESSBOOK:
        ADDRESSBOOK[name] = []
        ADDRESSBOOK[name].append(sanitize_contacts(phone_num))
    return f"Contact {name} with phone {sanitize_contacts(phone_num)} is added"

@input_error
def change_number(name: str, old_num: str, new_num): # Заміна старого номеру телефону на новий. Приклад: "change User_name 095-xxx-xx-xx 050-xxx-xx-xx"
    if name in ADDRESSBOOK:
        ADDRESSBOOK[name].remove(sanitize_contacts(old_num))
        ADDRESSBOOK[name].append(sanitize_contacts(new_num))
    return f"Changed contact {name} - old number {sanitize_contacts(old_num)} to new number {sanitize_contacts(new_num)}"

@input_error
def phone(name): # Пошук телефону за іменем контакту. Приклад : phone User_name
    phones = ""
    for i in ADDRESSBOOK[name]:
        phones += i + " "
    return phones

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
    hello_handler: ["hello"],
    add_handler: ["add", "додай", "+"],
    change_number: ["change"],
    phone:["phone"],
    exit_handler: ["good bye", "close", "exit"]
}


def main(): #цикл запит-відповідь
    while True:
        user_input = input(">>>") # add ...
        if not user_input:
            continue
        func, data = command_parser(user_input)
        print(func, data)
        result = func(*data)
        print(result)
        if func == exit_handler:
            break
        print(ADDRESSBOOK)
    
if __name__== "__main__":
    main()
