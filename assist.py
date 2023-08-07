
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
    return f"{normalized_name}'s phone number is {ADDRESSBOOK[name]}. "

@input_error
def show_all(*args): # Показати всі контакти. Приклад : show / show all
    if not ADDRESSBOOK:
        raise ValueError
    result = "Contacts:\n"
    for name, phone_num in ADDRESSBOOK.items():
        result += f"{name}: {phone_num}\n"
    return result

def print_error_output (message):
    print("Error: ", message)
        

@input_error
def main(): #цикл запит-відповідь для взаємодії з користувачем

    COMMANDS = {
    "hello": lambda: print("Hello, how can I help you?\n"),
    "show all": lambda: print(show_all()),
    "add": lambda: print(add_handler(user_devided[1], user_devided[2])) if len(user_devided) == 3 else print_error_output("write correct username and phone number."),
    "change": lambda: print(change_number(user_devided[1], user_devided[2])) if len(user_devided) == 3 else print_error_output("write name and phone."),
    "phone": lambda: print(get_phone(user_devided[1])) if len(user_devided) == 2 else print_error_output("write name."),
    "good bye": lambda: print("Good bye!"),
    "exit": lambda: print("Good bye!"),
    "close": lambda: print("Good bye!"),
    "end": lambda: print("Good bye!")
}
    while True:
        user_input = input("Enter command \t")
        user_devided = user_input.split(maxsplit=2)
        result_text = ""
        for char in user_input:
            if char != " ":
                result_text += char.lower()
            else:break
        
        if result_text in COMMANDS:
            COMMANDS[result_text]()
            if result_text in ["close", "exit", "end"]:
                break
        elif user_input.lower() in COMMANDS:
            COMMANDS[user_input.lower()]()
            if user_input.lower() == "good bye":
                break
        else:
            print("Uncorrect. Use the command 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'exit', 'close', 'end' " )
    
if __name__== "__main__":
    main()