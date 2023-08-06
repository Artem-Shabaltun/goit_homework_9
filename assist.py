
ADDRESSBOOK = {}

def input_error (inner): # Декоратор - для обробки помилок та виводу повідомлення
    def wrap(*args):
        try:
            return inner(*args)
        except KeyError:
            print("Enter correct username")
        except IndexError:
            print("Give me name and phone please")
        except ValueError:
            print("Enter username")
    return wrap

def sanitize_contacts(phone_num): # Функція для прийому різних форматів вводу номера
    new_phone = (
        phone_num.strip()
        .removeprefix("+38")
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
    sanitized_phone = sanitize_contacts(phone_num)
    normalized_name = name.title()
    if sanitized_phone:
        if normalized_name in ADDRESSBOOK:
            ADDRESSBOOK[normalized_name].append(sanitized_phone)
        else:
            ADDRESSBOOK[normalized_name] = [sanitized_phone]
        return f"Contact {normalized_name} with phone {sanitized_phone} is added"
    else:
        return "Invalid phone number format"

@input_error
def change_number(name: str, old_num: str, new_num): # Заміна старого номеру телефону на новий. Приклад: "change User_name 095-xxx-xx-xx 050-xxx-xx-xx"
    normalized_name = name.title()
    if normalized_name in ADDRESSBOOK:
        ADDRESSBOOK[normalized_name].remove(sanitize_contacts(old_num))
        ADDRESSBOOK[normalized_name].append(sanitize_contacts(new_num))
    return f"Changed contact {normalized_name} - old number {sanitize_contacts(old_num)} to new number {sanitize_contacts(new_num)}"

@input_error
def phone(name): # Пошук телефону за іменем контакту. Приклад : phone User_name
    normalized_name = name.title()
    if normalized_name in ADDRESSBOOK:
        phones = " ".join(ADDRESSBOOK[normalized_name])
        return f"{normalized_name}: {phones}\n"
    else:
        return f"Contact {normalized_name} not found"

@input_error
def show_all(*args): # Показати всі контакти. Приклад : show / show all
    text = ""
    for name_user, phone_list in ADDRESSBOOK.items():
        phones = " ".join(phone_list)
        text += f"{name_user}: {phones}\n"
    return text

def exit_handler(*args):
    return "Good bye!"


def command_parser(raw_str): # Парсер команд
    elements = raw_str.split()
    for key,value in COMMANDS.items():
        if elements[0].lower() in value:
            return key, elements [1:]
        

COMMANDS = {
    hello_handler:["hello"],
    add_handler:["add", "додай", "+"],
    change_number:["change"],
    phone:["phone"],
    show_all:["show all", "show"],
    exit_handler:["good bye", "close", "exit", "end"]
}

@input_error
def main(): #цикл запит-відповідь
    while True:
        user_input = input("Enter command:") # add >>>
        if not user_input:
            continue
        func, data = command_parser(user_input)
        # print(func, data)
        result = func(*data)
        print(result)
        if func == exit_handler:
            break
        print(ADDRESSBOOK)
    
if __name__== "__main__":
    main()
