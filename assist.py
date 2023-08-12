
ADDRESSBOOK = {}

def input_error (inner): # Декоратор - для обробки помилок та виводу повідомлення
    def wrap(*args, **kwargs):
        try:
            return inner(*args, **kwargs)
        except KeyError:
            print("Error: The contact not found")
        except ValueError:
            print("Error: Please enter username and phone number")
        except IndexError:
            print("Error: Please enter username and phone number")
    return wrap

def normalize_name(name):
    return name.upper() # Переводимо всі імена в верхній регістр для реалізації незалежності команд від регістру вводу.

def sanitize_contacts(phone_num): # Форматуємо номер телефону для списку контактів, незалежно від формату вводу
    new_phone = (
        phone_num.strip()
        .removeprefix("+38")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

@input_error
def add_handler(name, phone_num): # Додаємо контакт в список. Приклад: "add name 095-xxx-xx-xx"
    normalized_name = normalize_name(name)
    if normalized_name in ADDRESSBOOK:
        raise ValueError
    sanitize_phone = sanitize_contacts(phone_num)
    ADDRESSBOOK[normalized_name] = sanitize_phone
    return f"Contact {normalized_name} with phone {sanitize_phone} is added."

@input_error
def change_number(name: str, phone_num): # Заміна старого номеру телефону на новий. Приклад: "change name 050-xxx-xx-xx"
    normalized_name = normalize_name(name)
    if normalized_name not in ADDRESSBOOK:
        raise KeyError
    sanitize_phone = sanitize_contacts(phone_num)
    ADDRESSBOOK[normalized_name] = sanitize_phone
    return f"Changed contact {normalized_name} number to {sanitize_phone}."

@input_error
def get_phone(name): # Пошук телефону за іменем контакту. Приклад : phone name
    normalized_name = normalize_name(name)
    if normalized_name not in ADDRESSBOOK:
        raise KeyError
    return f"{normalized_name}'s phone number is {ADDRESSBOOK[normalized_name]}. "

@input_error
def show_all_command(*args): # Показати всі контакти. Приклад : show / show all
    if not ADDRESSBOOK:
        print_error_output("The contacts list is empty")
    else:
        try:
            result = "Contacts:\n"
            for name, phone_num in ADDRESSBOOK.items():
                result += f"{name}: {phone_num}\n"
            print(result)
        except ValueError as e:
            print_error_output(e)

def print_error_output (message):
    print("Error: ", message)
        
@input_error
def main(): #цикл запит-відповідь для сценаріїв взаємодії з користувачем

    COMMANDS = {
        "HELLO": hello,
        "SHOW ALL": show_all_command,
        "SHOW": show_all_command,
        "ADD": add,
        "CHANGE": change,
        "PHONE": phone,
        "GOOD BYE": goodbye,
        "EXIT": exit_program,
        "CLOSE": close_program,
        "END": end_program,
    }
    while True:
        user_input = input("Enter command: ").upper()
        user_devided = user_input.split(maxsplit=2)
        result_text = user_devided[0]
        
        if result_text in COMMANDS:
            COMMANDS[result_text](user_devided)
            if result_text in ["CLOSE", "EXIT", "END"]:
                break
        else:
            print("Incorrect command. Use the command 'HELLO', 'ADD', 'CHANGE', 'PHONE', 'SHOWALL', 'GOODBYE', 'EXIT', 'CLOSE', 'END' ")
    
def hello(args):
        print("Hello, how can I help you?")

def add(args):
        if len(args) == 3:
            print(add_handler(args[1], args[2]))
        else:
            print_error_output("Write correct username and phone number.")
    
def change(args):
    if len(args) == 3:
        print(change_number(args[1], args[2]))
    else:
        print_error_output("Write name and phone.")

def phone(args):
    if len(args) == 2:
        print(get_phone(args[1]))
    else:
        print_error_output("Write name.")

def goodbye(args):
    print("Good bye!")

def exit_program(args):
    print("Good bye!")
    exit()

def close_program(args):
    print("Good bye!")
    exit()

def end_program(args):
    print("Good bye!")
    exit()

if __name__== "__main__":
    main()